document.addEventListener('DOMContentLoaded', function () {
    const userInitials = document.getElementById('user-initials');
    const dropdownMenu = document.getElementById('dropdown-menu');
    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.getElementById('nav-links');

    // Toggle dropdown on initials click
    userInitials.addEventListener('click', function (e) {
        e.stopPropagation(); // Prevents the click from bubbling up and triggering the document click event
        dropdownMenu.classList.toggle('show'); // Toggle 'show' class to display the dropdown
    });

    // Toggle mobile nav menu
    menuToggle.addEventListener('click', function () {
        navLinks.classList.toggle('show');
    });

    // Close dropdown if clicked outside
    document.addEventListener('click', function (e) {
        if (!userInitials.contains(e.target)) {
            dropdownMenu.classList.remove('show'); // Remove 'show' class to hide the dropdown
        }
    });
});
