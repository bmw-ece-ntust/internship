import React, { useEffect, useRef } from 'react';
import { PanelProps } from '@grafana/data';
import { SimpleOptions } from 'types';
import { css, cx } from '@emotion/css';
import { useStyles2 } from '@grafana/ui';
import { PanelDataErrorView } from '@grafana/runtime';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

interface Props extends PanelProps<SimpleOptions> {}

const getStyles = () => {
  return {
    wrapper: css`
      font-family: Open Sans;
      position: relative;
    `,
    viewer: css`
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
    `,
    textBox: css`
      position: absolute;
      bottom: 0;
      left: 0;
      padding: 10px;
    `,
  };
};

export const SimplePanel: React.FC<Props> = ({ options, data, width, height, fieldConfig, id }) => {
  const styles = useStyles2(getStyles);
  const viewerRef = useRef<HTMLDivElement>(null); // Ref for the 3D viewer div

  useEffect(() => {
    if (!viewerRef.current) { return }; // Ensure ref is available

    // Set up the Scene, Camera, and Renderer
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(width, height);
    viewerRef.current.appendChild(renderer.domElement);

    // Orbit Controls for interactivity
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.25;
    controls.screenSpacePanning = false;
    controls.maxPolarAngle = Math.PI / 2;

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
    directionalLight.position.set(1, 1, 1).normalize();
    scene.add(directionalLight);

    // Load GLTF Model
    const loader = new GLTFLoader();
    loader.load('http://127.0.0.1:8000/output_scene_with_3d_mesh.glb', (gltf) => {
      scene.add(gltf.scene);

      // Center the camera on the model
      const box = new THREE.Box3().setFromObject(gltf.scene);
      const center = box.getCenter(new THREE.Vector3());
      const size = box.getSize(new THREE.Vector3());

      const maxDim = Math.max(size.x, size.y, size.z);
      const fov = camera.fov * (Math.PI / 180);
      const cameraZ = Math.abs(maxDim / 2 / Math.tan(fov / 2));

      camera.position.z = cameraZ * 1.5; // Adjust multiplier as needed
      controls.target.copy(center);
      controls.update();

      animate(); // Start animation loop
    }, undefined, (error) => {
      console.error('An error occurred loading the model:', error);
    });

    // Animation Loop
    const animate = () => {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    };

    // Handle resizing
    const onWindowResize = () => {
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    };

    window.addEventListener('resize', onWindowResize);

    return () => {
      // Clean up on unmount
      window.removeEventListener('resize', onWindowResize);
      if (viewerRef.current) {
        viewerRef.current.removeChild(renderer.domElement);
      }
    };
  }, [width, height]);

  if (data.series.length === 0) {
    return <PanelDataErrorView fieldConfig={fieldConfig} panelId={id} data={data} needsStringField />;
  }

  return (
    <div
      className={cx(
        styles.wrapper,
        css`
          width: ${width}px;
          height: ${height}px;
        `
      )}
    >
      <div ref={viewerRef} className={styles.viewer}></div>

      <div className={styles.textBox}>
        {options.showSeriesCount && (
          <div data-testid="simple-panel-series-counter">Number of series: {data.series.length}</div>
        )}
        <div>Text option value: {options.text}</div>
      </div>
    </div>
  );
};
