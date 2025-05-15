document.addEventListener('DOMContentLoaded', function() {
    // Trigger the modal for unauthenticated users
    const authModalExists = document.getElementById('authModal') !== null;
    if (authModalExists) {
        console.log("Auth modal exists, attempting to show it.");  // Debug
        try {
            var authModal = new bootstrap.Modal(document.getElementById('authModal'), {
                backdrop: 'static',  // Prevent closing by clicking outside
                keyboard: false      // Prevent closing with the Escape key
            });
            authModal.show();
            console.log("Auth modal shown successfully.");
        } catch (e) {
            console.error("Error showing auth modal:", e);
        }
    } else {
        console.log("Auth modal does not exist (user is likely authenticated).");
    }

    // Trigger the confirmation modal on the home page
    const confirmBookingModal = document.getElementById('confirmBookingModal');
    if (confirmBookingModal) {
        console.log("Confirm booking modal exists, checking query parameter.");  // Debug
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('booking_confirmed') === 'true') {
            console.log("Booking confirmed, showing modal.");  // Debug
            try {
                var confirmModal = new bootstrap.Modal(confirmBookingModal);
                confirmModal.show();
                console.log("Confirm booking modal shown successfully.");
            } catch (e) {
                console.error("Error showing confirm booking modal:", e);
            }
        }
    }

    // Booking form validation
    const bookingForm = document.getElementById('bookingForm');
    if (bookingForm) {
        const dateInput = document.querySelector('input[type="date"]');
        if (!dateInput) {
            console.error("Date input not found. Check if the event_date field is rendering as type='date'.");
        } else {
            console.log("Date input found:", dateInput);  // Debug

            const today = new Date('2025-05-15');  // Current date (May 15, 2025)
            const minDate = new Date(today);
            minDate.setDate(today.getDate() + 7);  // Minimum date is 7 days from today (May 22, 2025)

            bookingForm.addEventListener('submit', function(e) {
                console.log("Form submitted, validating date:", dateInput.value);  // Debug
                // Check if a date is selected
                if (!dateInput.value) {
                    e.preventDefault();
                    alert('Please select an event date.');
                    return;
                }

                // Validate the selected date
                const selectedDate = new Date(dateInput.value);
                if (selectedDate < today) {
                    e.preventDefault();
                    alert('You cannot book for a past date. Please select a future date.');
                    dateInput.value = '';  // Clear the invalid date
                } else if (selectedDate < minDate) {
                    e.preventDefault();
                    alert('Bookings must be made at least 7 days in the advance. Please select a later date.');
                    dateInput.value = '';  // Clear the invalid date
                } else {
                    console.log("Date validation passed, submitting form.");  // Debug
                }
            });

            dateInput.addEventListener('change', function() {
                const selectedDate = new Date(dateInput.value);
                if (selectedDate < today) {
                    alert('You cannot book for a past date. Please select a future date.');
                    dateInput.value = '';
                } else if (selectedDate < minDate) {
                    alert('Bookings must be made at least 7 days in advance. Please select a later date.');
                    dateInput.value = '';
                }
            });
        }
    } else {
        console.log("Booking form not found on this page.");
    }

    // Contact form validation
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const email = document.querySelector('input[type="email"]').value;
            if (!email.includes('@')) {
                e.preventDefault();
                alert('Please enter a valid email address.');
            }
        });
    }
});