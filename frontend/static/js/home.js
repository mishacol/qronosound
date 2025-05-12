document.getElementById('download-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = document.getElementById('url-input').value;
    const format = document.getElementById('format-select').value;
    const errorMessage = document.getElementById('error-message');

    // Validate URL
    try {
        const validateResponse = await fetch('/api/validate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });
        const validateData = await validateResponse.json();
        if (!validateData.valid) throw new Error(validateData.error);
    } catch (error) {
        errorMessage.textContent = error.message;
        errorMessage.classList.remove('hidden');
        return;
    }

    // Fetch audio
    try {
        const fetchResponse = await fetch('/api/fetch', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url, format })
        });
        const fetchData = await fetchResponse.json();
        if (fetchData.error) throw new Error(fetchData.error);
        errorMessage.classList.add('hidden');
        // TODO: Load audio into Wavesurfer.js
        console.log('Fetch success:', fetchData);
    } catch (error) {
        errorMessage.textContent = error.message;
        errorMessage.classList.remove('hidden');
    }
});