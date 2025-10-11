// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Test Button
    const testBtn = document.getElementById('testBtn');
    const result = document.getElementById('result');
    let clickCount = 0;

    testBtn.addEventListener('click', function() {
        clickCount++;
        result.textContent = `Button clicked ${clickCount} time${clickCount !== 1 ? 's' : ''}! 🎉`;
        
        // Animation effect
        result.style.transform = 'scale(1.1)';
        setTimeout(() => {
            result.style.transform = 'scale(1)';
        }, 200);
    });

    // Display Device Info
    displayDeviceInfo();

    // Cordova device ready event (if running as APK)
    document.addEventListener('deviceready', onDeviceReady, false);
});

function displayDeviceInfo() {
    // User Agent
    document.getElementById('userAgent').textContent = navigator.userAgent;

    // Screen Size
    const screenWidth = window.screen.width;
    const screenHeight = window.screen.height;
    document.getElementById('screenSize').textContent = `${screenWidth} x ${screenHeight}`;

    // Platform
    document.getElementById('platform').textContent = navigator.platform;
}

function onDeviceReady() {
    console.log('Cordova is ready!');
    
    // Update platform info with Cordova data if available
    if (typeof device !== 'undefined') {
        document.getElementById('platform').textContent = 
            `${device.platform} ${device.version} (Cordova)`;
    }

    // You can add more Cordova-specific features here
    // For example:
    // - Camera access
    // - Geolocation
    // - File system
    // - etc.
}

// Example: Show notification
function showNotification(message) {
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: #4CAF50;
        color: white;
        padding: 15px 30px;
        border-radius: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        z-index: 1000;
        animation: slideDown 0.3s ease-out;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideUp 0.3s ease-out';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Add animation keyframes
const style = document.createElement('style');
style.textContent = `
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateX(-50%) translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
    }
    
    @keyframes slideUp {
        from {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
        to {
            opacity: 0;
            transform: translateX(-50%) translateY(-20px);
        }
    }
`;
document.head.appendChild(style);
