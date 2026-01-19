<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Mathematical Wave Animation</title>

<style>
    body {
        margin: 0;
        background: radial-gradient(circle at top, #1a1a2e, #000);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        overflow: hidden;
        font-family: Arial, sans-serif;
    }

    canvas {
        box-shadow: 0 0 40px rgba(0, 200, 255, 0.4);
        border-radius: 12px;
    }

    .title {
        position: absolute;
        top: 20px;
        color: #fff;
        font-size: 22px;
        letter-spacing: 2px;
        opacity: 0.9;
    }
</style>
</head>

<body>

<div class="title">🌊 Mathematical Wave Animation</div>
<canvas id="waveCanvas" width="500" height="500"></canvas>

<script>
const canvas = document.getElementById("waveCanvas");
const ctx = canvas.getContext("2d");

const width = canvas.width;
const height = canvas.height;

let time = 0;

// Convert value to Cool-Warm color
function colorMap(value) {
    const r = Math.floor(255 * Math.max(value, 0));
    const b = Math.floor(255 * Math.max(-value, 0));
    const g = 80;
    return `rgb(${r}, ${g}, ${b})`;
}

function animate() {
    const image = ctx.createImageData(width, height);
    const data = image.data;

    for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {

            // Normalize coordinates
            const nx = (x - width / 2) / 80;
            const ny = (y - height / 2) / 80;

            // Same math as Python
            const z = Math.sin(nx * nx + ny * ny + time);

            const index = (y * width + x) * 4;
            const color = colorMap(z);

            const rgb = color.match(/\d+/g);
            data[index]     = rgb[0]; // Red
            data[index + 1] = rgb[1]; // Green
            data[index + 2] = rgb[2]; // Blue
            data[index + 3] = 255;    // Alpha
        }
    }

    ctx.putImageData(image, 0, 0);
    time += 0.1;
    requestAnimationFrame(animate);
}

animate();
</script>

</body>
</html>
