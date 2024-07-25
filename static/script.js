document.getElementById('predictForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get form data
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Send data to the Flask API
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // Display the prediction result
        document.getElementById('prediction').textContent = `$${result.predicted_expenses.toFixed(2)}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
