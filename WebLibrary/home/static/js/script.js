function getRandomPosition() {
    const maxWidth = window.innerWidth - 150;
    const maxHeight = window.innerHeight - 150;
    const randomX = Math.floor(Math.random() * maxWidth);
    const randomY = Math.floor(Math.random() * maxHeight);
    return { x: randomX, y: randomY };
}

function setRandomProperties(box) {
    const position = getRandomPosition();
    const randomSize = Math.floor(Math.random() * 100) + 50;
    const randomRotation = Math.floor(Math.random() * 360);

    const colors = ['#e74c3c', '#2ecc71', '#3498db', '#f1c40f', '#9b59b6'];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];

    const shapes = ['circle', 'square', 'star', 'triangle'];
    const randomShape = shapes[Math.floor(Math.random() * shapes.length)];

    box.style.top = `${position.y}px`;
    box.style.left = `${position.x}px`;
    box.style.width = `${randomSize}px`;
    box.style.height = `${randomSize}px`;
    box.style.backgroundColor = randomColor;
    box.style.transform = `rotate(${randomRotation}deg)`;

    box.classList.remove('circle', 'square', 'star', 'triangle');
    if (randomShape === 'circle') {
        box.style.borderRadius = '50%';
    } else {
        box.style.borderRadius = '0';
        box.classList.add(randomShape);
    }
}

function animateBoxes() {
    const boxes = document.querySelectorAll('.fun-animation');
    boxes.forEach(box => setRandomProperties(box));
}

document.addEventListener('DOMContentLoaded', () => {
    animateBoxes();
    setInterval(animateBoxes, 2000);
});