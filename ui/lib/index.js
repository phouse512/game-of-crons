var $ = require('jquery');
var request = require('request');
var THREE = require('three');

var container;
var camera, scene, renderer;

function init() {
    camera = new THREE.OrthographicCamera(window.innerWidth/ -2, window.innerWidth/2, 
                                          window.innerHeight/2, window.innerHeight/-2, -500, 1000);

    camera.position.x = 200;
    camera.position.y = 100;
    camera.position.z = 200;

    scene = new THREE.Scene();

    displayGrid(500, 50);

    var ambientLight = new THREE.AmbientLight(Math.random() * 0x10);
    scene.add(ambientLight);



    renderer = new THREE.WebGLRenderer();
    renderer.setClearColor(0xf0f0f0);
 //   renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
}

function displayGrid(size, step) {
    var geometry = new THREE.Geometry();

    for (var i = -size; i <= size; i += step) {
        geometry.vertices.push(new THREE.Vector3(-size, 0, i));
        geometry.vertices.push(new THREE.Vector3(size, 0, i));

        geometry.vertices.push(new THREE.Vector3(i, 0, -size));
        geometry.vertices.push(new THREE.Vector3(i, 0, size));
    }

    var material = new THREE.LineBasicMaterial( { color: 0x000000, opacity: 0.2 });
    var line = new THREE.LineSegments(geometry, material);

    scene.add(line);
}

function appStart() {
    console.log('yoza');
    init();
    render();
}

function render() {
    requestAnimationFrame(render);
    camera.lookAt(scene.position);
    renderer.render(scene, camera);
}

$(document).ready(function() {
    appStart();
});

