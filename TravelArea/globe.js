
// Create a scene which will hold all our meshes to be rendered
var scene = new THREE.Scene();

// Create and position a camera
var camera = new THREE.PerspectiveCamera(
    75, // Field of view
    window.innerWidth / window.innerHeight, // Aspect ratio
    0.1, // Near clipping pane
    1000 // Far clipping pane
);

// Reposition the camera
camera.position.z = 5;

// Point the camera at a given coordinate
camera.lookAt(new THREE.Vector3(0, 0, 0))

// Create a renderer
var renderer = new THREE.WebGLRenderer({ antialias: true });

// Size should be the same as the window
renderer.setSize(window.innerWidth, window.innerHeight);

// Set a near white clear color (default is black)
renderer.setClearColor('#060606');

// Append to the document
document.body.appendChild( renderer.domElement );

// Create orbit controls
var controls = new THREE.OrbitControls(camera, renderer.domElement);

// Create a sphere geometry
var sphereGeometry = new THREE.SphereGeometry(1, 32, 32);

// Create a material for the sphere
var sphereMaterial = new THREE.MeshBasicMaterial({
    map: new THREE.TextureLoader().load('earthmap1k.jpg'),
  });

// Create the sphere mesh
var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);

// Add the sphere to the scene
scene.add(sphere);

class Pin {
    constructor(name, mesh, coordinates, phi, theta) {
        this.name = name;
        this.mesh = mesh;
        this.coordinates = coordinates;
        this.phi = phi;
        this.theta = theta;
    }
}

// Create an empty array to store the pin objects
var pins = [];
var curves = [];

// Function to add coordinates to the list and create pins
function addCoordinates(name, lat, lon) {
    console.log("adding pin");
    // Create an object to hold the latitude and longitude
    var coordinate = {
        latitude: lat,
        longitude: lon
    };

    console.log(coordinate);

    // Create a pin and add it to the scene
    var pinGeometry = new THREE.SphereGeometry(0.02, 32, 32);
    var pinMaterial = new THREE.MeshBasicMaterial({ color: 0x9F3EAC });
    var pinMesh = new THREE.Mesh(pinGeometry, pinMaterial);
    scene.add(pinMesh);

    // Push the pin object to the pins array
    phi =  (coordinate.longitude) * (Math.PI / 180) + Math.PI + 29*Math.PI/32;
    theta = Math.PI /2 - ((coordinate.latitude) * (Math.PI / 180) + sphere.rotation.y);
    console.log(phi, theta);
    var pin = new Pin(name, pinMesh, coordinate, phi, theta);
    pins.push(pin);
    enclosedSections.addToScene(phi, theta);
}

// Update the pin positions in the animation loop
function animate(radius) {
    requestAnimationFrame(animate);

    // Rotate the globe
    sphere.rotation.y += 0.0000;

    // Update pin positions and rotations
    for (var i = 0; i < pins.length; i++) {
        var pin = pins[i];

        // Convert the latitude and longitude to spherical coordinates
        var phi = -((pin.coordinates.longitude) * (Math.PI / 180));
        var theta = Math.PI / 2 - ((pin.coordinates.latitude) * (Math.PI / 180) + sphere.rotation.y);
        pin.phi = phi;
        pin.theta = theta;

        // Calculate the position of the pin
        var pinRadius = 1.0; // Distance slightly above the sphere's surface
        pin.mesh.position.x = pinRadius * Math.sin(theta) * Math.cos(phi);
        pin.mesh.position.y = pinRadius * Math.cos(theta);
        pin.mesh.position.z = pinRadius * Math.sin(theta) * Math.sin(phi);

        // Rotate the pin with the globe
        pin.mesh.rotation.y += 0.0000;
    }

    // Update curve positions and rotations
    for (var i = 0; i < curves.length; i++) {
        var curve = curves[i][0];
        var curveMesh = curves[i][1];

        var points = curve.getPoints(50); // Adjust the resolution as needed
        var positions = new Float32Array(points.length * 3);
        for (var i = 0; i < points.length; i++) {
            positions[i * 3] = points[i].x;
            positions[i * 3 + 1] = points[i].y;
            positions[i * 3 + 2] = points[i].z;
        }
        curveMesh.geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        //console.log("Positions:", curveMesh.positions);
    }

    // Update OrbitControls
    controls.update();

    // Render the scene/camera combination
    renderer.render(scene, camera);
}

// Call the addCoordinates function inside the placePin function
function placePin(name, lat, lon, radius) {
    // ... existing code to place the pin ...

    // Add the coordinates and create a pin
    addCoordinates(name, lat, lon);

    // Adds name to list
    var li = document.createElement('li');
    li.textContent = name;
    document.getElementById('locationList').appendChild(li);

    // Start the animation if it hasn't already started
    if (pins.length >= 1) {
        animate(radius);
    }
}

document.getElementById('addLocation').addEventListener('click', async function() {
    var location = document.getElementById('locationInput').value;
    console.log(location);

    try {
        const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${location}`);
        const data = await response.json();
        console.log(data);

        if (data.length > 0) {
            var lat = parseFloat(data[0].lat);
            var lon = parseFloat(data[0].lon);

            placePin(location, lat, lon, 1);
        } else {
            console.log('Location not found');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

animate(1);

loadDataFromCookie('GlobePins');

document.getElementById('runButton').addEventListener('click', async function() {
    saveDataToCookie('GlobePins', 90);
});


//-------COOKIES-------

function setCookie(name,value,days) {
    var expires = "";
    if (days) {
      var date = new Date();
      date.setTime(date.getTime() + (days*24*60*60*1000));
      expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
  }

  function saveDataToCookie(name, days) {
    // Convert the pins array to a JSON string
    var coords = {};
    for (i = 0; i< pins.length; i++) {
        coords[pins[i].name] = [pins[i].coordinates.latitude, pins[i].coordinates.longitude];
    }
    var value = JSON.stringify(coords);

    // Save the JSON string as a cookie
    setCookie(name, value, days);
  }

  function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
      var c = ca[i];
      while (c.charAt(0)==' ') c = c.substring(1,c.length);
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
  }

  function loadDataFromCookie(name) {
    // Get the JSON string from the cookie
    var jsonString = getCookie(name);

    if (jsonString) {
        // Parse the JSON string to an array of objects
        var data = JSON.parse(jsonString);
        console.log(Object.keys(data));
        for (i = 0; i<Object.keys(data).length; i++) {
            console.log("Lat and Lon", data[Object.keys(data)[i]][0], data[Object.keys(data)[i]][1]);
            placePin(Object.keys(data)[i], data[Object.keys(data)[i]][0], data[Object.keys(data)[i]][1], 1);
        }
    }
  }