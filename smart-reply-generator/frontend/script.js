document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const charCount = document.querySelector('.char-count');
    const generateBtn = document.getElementById('generate-btn');
    const resultsSection = document.getElementById('results-section');
    const intentDisplay = document.getElementById('intent-display');
    const confidenceDisplay = document.getElementById('confidence-display');
    const repliesContainer = document.getElementById('replies-container');
    const historySection = document.getElementById('history-section');
    const historyList = document.getElementById('history-list');

    // Update character count
    userInput.addEventListener('input', () => {
        const count = userInput.value.length;
        charCount.textContent = `${count} characters`;
    });

    // Handle Generation
    generateBtn.addEventListener('click', async () => {
        const message = userInput.value.trim();
        
        if (!message) {
            alert('Please enter a message first!');
            return;
        }

        setLoading(true);

        try {
            const response = await fetch('/api/generate-replies', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });

            if (!response.ok) throw new Error('Failed to fetch replies');

            const data = await response.json();
            displayResults(data);
            addToHistory(message, data);
            
        } catch (error) {
            console.error('Error:', error);
            alert('Something went wrong. Is the server running?');
        } finally {
            setLoading(false);
        }
    });

    function setLoading(isLoading) {
        if (isLoading) {
            generateBtn.classList.add('loading');
            generateBtn.querySelector('.btn-text').textContent = 'Analyzing...';
            resultsSection.classList.add('hidden');
        } else {
            generateBtn.classList.remove('loading');
            generateBtn.querySelector('.btn-text').textContent = 'Generate Smart Replies';
        }
    }

    function displayResults(data) {
        resultsSection.classList.remove('hidden');
        resultsSection.classList.add('animate-in');
        
        intentDisplay.textContent = data.intent;
        confidenceDisplay.textContent = `${Math.round(data.confidence * 100)}%`;
        
        repliesContainer.innerHTML = '';
        
        data.replies.forEach((reply, index) => {
            const card = document.createElement('div');
            card.className = 'reply-card animate-in';
            card.style.animationDelay = `${index * 0.1}s`;
            
            card.innerHTML = `
                <span class="reply-text">${reply}</span>
                <span class="copy-icon">📋</span>
            `;

            card.addEventListener('click', () => {
                copyToClipboard(reply, card);
            });

            repliesContainer.appendChild(card);
        });
    }

    function addToHistory(query, data) {
        historySection.classList.remove('hidden');
        
        const historyItem = document.createElement('div');
        historyItem.className = 'history-item animate-in';
        
        historyItem.innerHTML = `
            <p class="history-query">"${query}"</p>
            <p class="history-intent">${data.intent}</p>
        `;
        
        historyList.prepend(historyItem);
    }

    async function copyToClipboard(text, element) {
        try {
            await navigator.clipboard.writeText(text);
            const originalIcon = element.querySelector('.copy-icon').textContent;
            element.querySelector('.copy-icon').textContent = '✅';
            setTimeout(() => {
                element.querySelector('.copy-icon').textContent = originalIcon;
            }, 2000);
        } catch (err) {
            console.error('Failed to copy: ', err);
        }
    }
});
