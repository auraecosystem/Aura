# AURA Design System



```js
import lottie from 'lottie-web';

// Universally compatible framework for pure web DOM or encapsulated mobile views
const animation = lottie.loadAnimation({
  container: document.getElementById('web4app-ui-layer'), 
  renderer: 'svg', // Draws native vector elements instead of heavy WebGL layers
  loop: true,
  autoplay: true,
  path: 'assets/3d_flattened_motion.json' 
});
```
## Theme
```theme.css
Cyber Web4
AI
Glassmorphism
Neon
Dark
```
---

## Colors
```css
Background:
#090B12

Surface:
#151A27

Primary:
#00D1FF

Secondary:
#00FFE0

Accent:
#7A5FFF

Danger:
#FF4B6E

Success:
#1DFF8A
```
---

## Typography
```pmx
Heading:
Space Grotesk

Body:
Inter

Code:
JetBrains Mono
```
---

## Border Radius
```css
12px

20px

32px
```
---

## Shadow
```css
0 0 30px rgba(0,209,255,.25)
```
---

## Buttons
```jss
Filled Neon

Glass

Outline

Ghost
```
---

## Cards
```html
Glass
Animated Border
Glow Hover
```
---

## Motion
```.gltf
300ms

Cubic-bezier

Particles

Grid

Glow

Mouse Trail

Parallax
```
---

## Icons
```icon.css
Lucide

Heroicons

Phosphor
```
---

## Layout
```tmpl
12 Column Grid

1440px Container

32px Gap

120px Section Padding
```
---

## Components
```glb
Navbar

Hero

Projects

AI Cards

Blockchain Cards

Blog Cards

Timeline

Stats

CTA

Footer
```

```jsx
import React, { useRef, useEffect } from 'react';
import { StyleSheet, View, Platform } from 'react-native';
import { Canvas } from '@react-three/fiber';
import { useGLTF, useAnimations } from '@react-three/drei';

// This single functional component renders flawlessly on Web, iOS, and Android
function AnimatedModel({ url }) {
  const modelRef = useRef();
  
  // Loads the universal .glb/.gltf extension dynamically 
  const { scene, animations } = useGLTF(url);
  const { actions } = useAnimations(animations, modelRef);

  useEffect(() => {
    // Detects and kicks off the 3D asset's baked animation timelines
    if (actions && animations.length > 0) {
      const firstAnimationName = Object.keys(actions)[0];
      actions[firstAnimationName].play();
    }
  }, [actions, animations]);

  return <primitive ref={modelRef} object={scene} />;
}

export default function App() {
  return (
    <View style={styles.container}>
      <Canvas>
        <ambientLight intensity={0.7} />
        <directionalLight position={[10, 10, 5]} intensity={1.5} />
        
        {/* URL points to your cross-platform asset bundle */}
        <AnimatedModel url={Platform.OS === 'web' ? '/assets/ui.glb' : './assets/ui.glb'} />
      </Canvas>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000' },
});
```

```swift
import SwiftUI
import RealityKit

struct Custom3DView: View {
    var body: some View {
        // Loads a native 3D/AR extension file and activates its layout
        ARViewContainer().edgesIgnoringSafeArea(.all)
    }
}

struct ARViewContainer: UIViewRepresentable {
    func makeUIView(context: Context) -> ARView {
        let arView = ARView(frame: .zero)
        
        // Code loads model entity via the .usdz extension name
        if let modelEntity = try? Entity.loadModel(named: "ui_animation.usdz") {
            let anchor = AnchorEntity()
            anchor.addChild(modelEntity)
            arView.scene.addAnchor(anchor)
            
            // Fires any baked animation configurations inside the extension file
            modelEntity.availableAnimations.forEach { modelEntity.playAnimation($0.repeat()) }
        }
        return arView
    }
    
    func updateUIView(_ uiView: ARView, context: Context) {}
}

```
[.splinecode](Spline-3D-Embed.md)

```js
import { Application } from '@splinetool/runtime';

const canvas = document.getElementById('canvas3d');
const app = new Application(canvas);

// Loads the compiled 3D interactive UI extension directly from your code asset folder
app.load('./scene.splinecode'); 
```

```jsx
import lottie from 'lottie-web';

lottie.loadAnimation({
  container: document.getElementById('ui-container'), // Target HTML div
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'animation.json' // Path to your code file extension
});

```
`.pmx`/
`.pmd` and `.vmd` (MikuMikuDance formats)To load native [MMD character models](.pmx/.pmd) and their raw motion data (.vmd) directly in code
```js
import { MMDLoader } from 'three/examples/jsm/loaders/MMDLoader.js';

const loader = new MMDLoader();

// First parameter: The character file (.pmx)
// Second parameter: The animation track file (.vmd)
loader.loadWithAnimation('character.pmx', 'motion.vmd', (mmd) => {
    const mesh = mmd.mesh;
    const animation = mmd.animation; // Rigged bones animation data
    
    // Apply animation directly to the MMD character mesh
    const mixer = new AnimationMixer(mesh);
    mixer.clipAction(animation).play();
});

```
[`.fbx`](Autodesk-Filmbox.md)
```jsx
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js';
import { AnimationMixer } from 'three';

const loader = new FBXLoader();

loader.load('animation.fbx', (fbx) => {
    // FBX files natively embed their animations directly on the main object
    const mixer = new AnimationMixer(fbx);
    const action = mixer.clipAction(fbx.animations[0]);
    action.play();
});

```
`.gltf` and `.glb` (The Web Standards)These are the most efficient formats for web UI. 
.gltf stores data in JSON text, while [.glb
](self-contained.md) binary file.
```js
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { AnimationMixer } from 'three';

const loader = new GLTFLoader();

// Load the extension
loader.load('model.gltf', (gltf) => {
    const model = gltf.scene;
    
    // Read and play the embedded animation data
    const mixer = new AnimationMixer(model);
    const clips = gltf.animations; // Array of animation clips
    const action = mixer.clipAction(clips[0]);
    action.play();
});

```
```html
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web 4 App 3D Canvas</title>
    <!-- Three.js Core CDN -->
    <script src="Use code with caution.htmlhttps://cloudflare.comUse code with caution.html"></script>
    <!-- GLTF Extension Loader CDN -->
    <script src="https://jsdelivr.net"></script>
</head>
<body style="margin: 0; overflow: hidden; background: #111;">

    <div id="canvas-container" style="width: 100vw; height: 100vh;"></div>

    <script>
        const container = document.getElementById('canvas-container');
        
        // 1. Setup Universal Web View Scene Engine
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        container.appendChild(renderer.domElement);

        // 2. Add Lighting Assets 
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
        scene.add(ambientLight);

        // 3. Process the Extension Code Structure
        let mixer;
        const loader = new THREE.GLTFLoader();
        
        loader.load('assets/ui_animation.glb', function (gltf) {
            const model = gltf.scene;
            scene.add(model);

            // Execute the animation frames over local runtime ticks
            mixer = new THREE.AnimationMixer(model);
            gltf.animations.forEach((clip) => {
                mixer.clipAction(clip).play();
            });
        });

        camera.position.z = 5;
        const clock = new THREE.Clock();

        // 4. Animation Frame Loop for Mobile App Sync
        function animate() {
            requestAnimationFrame(animate);
            const delta = clock.getDelta();
            if (mixer) mixer.update(delta); // Keeps animation processing fluid on mobile processors
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>

