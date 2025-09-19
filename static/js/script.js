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

    // New code for fetching and displaying short student info on index.html
    const form = document.getElementById('searchForm');
    const enrollInput = document.getElementById('enroll_no');
    const shortInfoDiv = document.getElementById('student-short-info');
    const shortEnrollment = document.getElementById('short-enrollment');
    const shortName = document.getElementById('short-name');
    const shortCourse = document.getElementById('short-course');
    const shortYear = document.getElementById('short-year');

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const enrollValue = enrollInput.value.trim();
            if (enrollValue.length < 3) {
                alert('Please enter a valid enrollment number (minimum 3 characters)');
                enrollInput.focus();
                return;
            }

            // Clear previous info
            shortEnrollment.textContent = '';
            shortName.textContent = '';
            shortCourse.textContent = '';
            shortYear.textContent = '';
            shortInfoDiv.style.display = 'none';

            fetch(`/api/student/${enrollValue}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Student not found');
                    }
                    return response.json();
                })
                .then(data => {
                    shortEnrollment.textContent = data.enrollment;
                    shortName.textContent = data.name;
                    shortCourse.textContent = data.course;
                    shortYear.textContent = data.year;
                    shortInfoDiv.style.display = 'block';

                    // Make enrollment clickable to open detailed page
                    shortEnrollment.classList.add('clickable-enrollment');
                    shortEnrollment.style.color = 'blue';
                    shortEnrollment.style.textDecoration = 'underline';
                    shortEnrollment.style.cursor = 'pointer';
                    shortEnrollment.onclick = () => {
                        window.location.href = `/student/${data.enrollment}`;
                    };
                })
                .catch(error => {
                    alert(error.message);
                });
        });
    }
});
