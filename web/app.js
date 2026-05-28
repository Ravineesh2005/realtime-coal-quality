// Clock functionality
function updateTime() {
    const now = new Date();
    document.getElementById('current-time').textContent = now.toLocaleTimeString();
}
setInterval(updateTime, 1000);
updateTime();

// Chart.js Setup for Quality Trend
const ctx = document.getElementById('trendChart').getContext('2d');
const trendChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['T-9', 'T-8', 'T-7', 'T-6', 'T-5', 'T-4', 'T-3', 'T-2', 'T-1', 'Now'],
        datasets: [{
            label: 'Visual Model GCV (kcal)',
            data: [5800, 5820, 5790, 5810, 5900, 5850, 5830, 5870, 5840, 5800],
            borderColor: '#3b82f6',
            backgroundColor: 'rgba(59, 130, 246, 0.1)',
            tension: 0.4,
            fill: true
        },
        {
            label: 'Physical Model GCV (kcal)',
            data: [5780, 5810, 5795, 5800, 5880, 5860, 5820, 5880, 5850, 5790],
            borderColor: '#10b981',
            backgroundColor: 'rgba(16, 185, 129, 0.1)',
            tension: 0.4,
            fill: true
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                min: 5000,
                max: 6500,
                grid: {
                    color: 'rgba(255, 255, 255, 0.05)'
                },
                ticks: { color: '#94a3b8' }
            },
            x: {
                grid: {
                    color: 'rgba(255, 255, 255, 0.05)'
                },
                ticks: { color: '#94a3b8' }
            }
        },
        plugins: {
            legend: {
                labels: { color: '#f8fafc' }
            }
        }
    }
});

// Simulation of real-time data incoming from backend
function simulateDataStream() {
    // Generate slight variations
    const visualGCV = Math.floor(5800 + (Math.random() * 200 - 100));
    let physicalGCV = visualGCV + Math.floor(Math.random() * 50 - 25);
    
    // Simulate an anomaly 10% of the time
    const isAnomaly = Math.random() < 0.1;
    if (isAnomaly) {
        physicalGCV -= 400; // Big discrepancy
    }

    // Update UI elements
    updatePredictionUI('visual', visualGCV);
    updatePredictionUI('physical', physicalGCV);
    
    // Update Sensors
    document.getElementById('sensor-moisture').textContent = (8.0 + Math.random()).toFixed(1) + '%';
    document.getElementById('sensor-ash').textContent = (12.0 + Math.random()*2).toFixed(1) + '%';
    document.getElementById('sensor-volatile').textContent = (25.0 + Math.random()).toFixed(1) + '%';
    document.getElementById('sensor-gcv').textContent = physicalGCV + ' kcal';

    // Discrepancy Check
    const diff = Math.abs(visualGCV - physicalGCV);
    const alertBanner = document.getElementById('alert-banner');
    if (diff > 300) {
        alertBanner.classList.remove('hidden');
    } else {
        alertBanner.classList.add('hidden');
    }

    // Update Chart
    trendChart.data.datasets[0].data.shift();
    trendChart.data.datasets[0].data.push(visualGCV);
    
    trendChart.data.datasets[1].data.shift();
    trendChart.data.datasets[1].data.push(physicalGCV);
    trendChart.update();
}

function updatePredictionUI(type, gcv) {
    const elGrade = document.getElementById(`${type}-grade`);
    const elConf = document.getElementById(`${type}-conf`);
    const parent = elGrade.parentElement;

    let grade = "Medium Grade";
    let cls = "medium-grade";
    
    if (gcv > 5900) {
        grade = "High Grade";
        cls = "high-grade";
    } else if (gcv < 5600) {
        grade = "Low Grade";
        cls = "low-grade";
    }

    elGrade.textContent = grade;
    elConf.textContent = (85 + Math.random() * 10).toFixed(1) + "%";
    
    parent.className = `prediction-value ${cls}`;
}

// Camera Connection Logic
const connectCameraBtn = document.getElementById('connect-camera-btn');
const videoFeed = document.getElementById('live-camera-feed');
const cameraOverlayText = document.getElementById('camera-overlay-text');
const scanningLine = document.getElementById('scanning-line');

connectCameraBtn.addEventListener('click', async () => {
    try {
        connectCameraBtn.textContent = "Connecting...";
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoFeed.srcObject = stream;
        
        // Update UI
        connectCameraBtn.style.display = 'none';
        cameraOverlayText.style.display = 'none';
        scanningLine.style.display = 'block'; // Show scanning line over video
    } catch (err) {
        console.error("Error accessing camera:", err);
        connectCameraBtn.textContent = "Access Denied";
        alert("Unable to access camera. Please ensure permissions are granted.");
    }
});

// Start simulation loop every 2 seconds
setInterval(simulateDataStream, 2000);
