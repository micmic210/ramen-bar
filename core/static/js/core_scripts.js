// Success Modal
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('reservationForm');
    const successModal = new bootstrap.Modal(document.getElementById('reservationSuccessModal'));
    
    form.addEventListner('submit', function (event) {
        event.preventDefault(); // Prevent form submission for demo purposes
        successModal.show();
    });
}); 

// Cancel Modal
    document.addEventListener('DOMContentLoaded', function () {
        const cancelModal = document.getElementById('cancelModal');
        const cancelForm = document.getElementById('cancelForm');

        cancelModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget; // Button that triggered the modal
            const reservationId = button.getAttribute('data-reservation-id'); // Extract info from data-* attributes
            cancelForm.action = `/cancel-reservation/${reservationId}/`;
        });
    }); 