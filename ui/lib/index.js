var $ = require('jquery');
var request = require('request');
var THREE = require('three');


function appStart() {
    console.log('yoza');
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    var geometry = new THREE.BoxGeometry(1, 1, 1);
    material = new THREE.MeshBasicMaterial( { color: 0x00ff00 });
    cube = new THREE.Mesh(geometry, material);

    scene.add(cube);

    camera.position.z = 5;

    render();
}

function render() {

    cube.rotation.x += 0.1;
    cube.rotation.y += 0.1;
    requestAnimationFrame(render);
    renderer.render(scene, camera);
}

$(document).ready(function() {
    appStart();
});

