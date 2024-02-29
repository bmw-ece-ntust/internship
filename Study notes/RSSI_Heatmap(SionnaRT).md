>Lauren Christy (TEEP)

> [!WARNING]
> This note hasn't been tested yet. Additional notes is going to be added, including testing results and adjustable codes.

# Sionna RT

## Main Reference:
- Discussion with Fayçal Aït Aoudia (Senior Research Scientist at NVIDIA)
- [Sionna Ray Tracing](https://nvlabs.github.io/sionna/api/rt.html#coverage-map)
- [Ray Tracing from NVIDIA's website](https://developer.nvidia.com/discover/ray-tracing)

## Key Takeaway:
- Usage of Sionna RT's ability to generate pathloss heatmaps for generating the RSSI Heatmap. Transmit power from scene's instance (`sionna.rt.Scene.coverage_map`) can be used to calculate the RSSI.

## Sionna RT Overview
Sionna™ is an open-source Python library for link-level simulations of digital communication systems built on top of the open-source software library TensorFlow for machine learning.

Sionna is a tool created and continually improved by NVIDIA. It's used for researching 5G and 6G technologies. It helps with complex simulations involving multiple users and connections. It uses codes that follow 5G standards, like LDPC. Plus, it has features for estimating channels, correcting errors, and decoding signals. Each part of Sionna works independently, so it's easy to test and change according to the needs.

## Ray Tracing (Background Information)
Ray tracing is a rendering technique that can realistically simulate the lighting of a scene and its objects by rendering physically accurate reflections, refractions, shadows, and indirect lighting. Ray tracing generates computer graphics images by tracing the path of light from the view camera, through the 2D viewing plane, out into the 3D scene, and back to the light sources. 

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/raytracing.jpg">


As it traverses the scene, there are three cases that can happen with the light:
- Reflect from one object to another (causing reflections)
- Blocked by objects (causing shadows)
- Pass through transparent or semi-transparent objects (causing refractions).
  
All of these interactions are combined to produce the final color and illumination of a pixel that is then displayed on the screen. This reverse tracing process of eye/camera to light source is chosen because it is far more efficient than tracing all light rays emitted from light sources in multiple directions.

## Ray Tracing (SionnaRT Module)
Sionna RT is a ray tracing extension for radio propagation modeling which is built on top of Mitsuba 3 and TensorFlow. Like all of Sionna’s components, it is differentiable. 

Sionna RT relies on Mitsuba 3 for the rendering and handling of scenes. Mitsuba 3 is a rendering system for forward and inverse light-transport simulation.

## Components
- ### Scene
  
  It's the most important component of the ray tracer. A scene is a collection of multiple instances of SceneObject which define the geometry and materials of the objects in the scene. The scene also includes transmitters (Transmitter) and receivers (Receiver)
  
  It has methods for the computation of propagation Paths (compute_paths()) and CoverageMap (coverage_map()).

  Scene example (`sionna.rt.scene.munich`) 

  <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/munich.png">

  - #### Coverage Maps
    
    In the case of displaying RSSI Heatmap from multiple access points, `sionna.rt.Scene.coverage_map` might be the correct one to use. This function computes a coverage map for every transmitter in the scene.

    For a given transmitter, a coverage map is a rectangular surface with arbitrary orientation subdivded into rectangular cells of size . The parameter `cm_cell_size` therefore controls the granularity of the map. The coverage map associates with every cell $(i,j)$ the quantity
    
    $b_{i, j}=\frac{1}{|C|} \int_{C_{i, j}}|h(s)|^2 d s$

    where $h(s)|^2$ is the squared amplitude of the path coefficients $a_{i}$ at position $s = (x,y)$, the integral is over the cell $C_{i, j}$, and $ds$ is the infinitesimal small surface element $d s=d x \cdot d y$. The dimension indexed by $i(j)$ corresponds to the $y(x)$-axis of the coverage map in its local coordinate system.

    Example
    ```
    import sionna
    from sionna.rt import load_scene, PlanarArray, Transmitter, Receiver
    scene = load_scene(sionna.rt.scene.munich)

    # Configure antenna array for all transmitters
    scene.tx_array = PlanarArray(num_rows=8,
                            num_cols=2,
                            vertical_spacing=0.7,
                            horizontal_spacing=0.5,
                            pattern="tr38901",
                            polarization="VH")

    # Configure antenna array for all receivers
    scene.rx_array = PlanarArray(num_rows=1,
                            num_cols=1,
                            vertical_spacing=0.5,
                            horizontal_spacing=0.5,
                            pattern="dipole",
                            polarization="cross")
    # Add a transmitters
    tx = Transmitter(name="tx",
                position=[8.5,21,30],
                orientation=[0,0,0])
    scene.add(tx)
    tx.look_at([40,80,1.5])

    # Compute coverage map
    cm = scene.coverage_map(cm_cell_size=[1.,1.],
                        num_samples=int(10e6))

    # Visualize coverage in preview
    scene.preview(coverage_map=cm,
                resolution=[1000, 600])
    ```

    Result

    <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/coverage_map_preview.png">
