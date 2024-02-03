document.addEventListener('DOMContentLoaded', function() { // whats happening here?
    loadNotes();
});

function loadNotes() {
    fetch('/notes')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById('notesArea').value = data.notes;
        })
        .catch(error => console.error('Error:', error));
}

function saveNotes() {
    const notes = document.getElementById('notesArea').value;
    fetch('/notes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `note=${encodeURIComponent(notes)}`
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}
