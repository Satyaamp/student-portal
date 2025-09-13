document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('input').forEach(input => {
        input.addEventListener('mouseover', () => {
            input.classList.add('bg-gray-100');
        });
        input.addEventListener('mouseout', () => {
            input.classList.remove('bg-gray-100');
        });
        input.addEventListener('touchstart', () => {
            input.classList.toggle('bg-gray-100');
        });
    });
});
