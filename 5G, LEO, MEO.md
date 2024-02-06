# Understanding 5G, LEO, and MEO

## :book: 5G
5G technology represents a significant advancement in wireless communication, offering a theoretical peak speed of 20 Gbps, substantially faster than the 1 Gbps peak speed of 4G. It not only provides improved speed but also promises **lower latency**, enhancing various digital experiences like online gaming, videoconferencing, and autonomous vehicles.

Unlike its predecessors, 5G goes beyond mere connectivity, aiming to deliver connected experiences from the cloud to clients. This technology features **virtualization, software-driven networks, and cloud integration.** It enables seamless mobility, allowing users to transition between cellular and Wi-Fi access without interruption.
![image](https://hackmd.io/_uploads/rJfNlfIK6.png)

5G is expected to simplify connectivity in underserved rural areas and urban centers facing high demand. The architecture involves distributed access points and brings data processing closer to users, ensuring faster processing. Additionally, 5G networks introduce software-defined platforms with advanced automation, supporting network slices that cater to specific user and device requirements.

The technology works by utilizing 5G New Radio, which covers a broader spectrum than 4G. Massive MIMO technology enhances data transfer by allowing multiple transmitters and receivers to operate simultaneously. **5G architectures are software-defined**, making them agile and flexible, with the ability to create network slices based on user needs. Machine learning-enabled automation further enhances digital experiences, especially in applications requiring rapid response times.

The real-world impact of 5G extends to various industries. In healthcare, it enables continuous patient monitoring through connected devices, providing real-time health data. In the automotive sector, 5G, combined with machine learning, facilitates information sharing among vehicles, enhancing road safety.


## :book: LEO and MEO
![image](https://hackmd.io/_uploads/r13wMK0_6.png)

 **Orbit Name**  |           **Altitude [km]**          | 
|:----------:|:----------------------------------:|
|  LEO | 	160 to 2000        | 
|  MEO |    2000 to <35786     |

When selecting a solution, users often overlook the importance of satellites, yet they play a vital role in communication links. Satellites are categorized into three types based on their orbits: LEO (Low Earth Orbit), MEO (Medium Earth Orbit), and GEO (Geostationary Earth Orbit). This discussion will primarily focus on LEO and MEO.

LEO and MEO represent the extremes of altitude, with LEO satellites being smaller and orbiting closer to Earth. Consequently, the rockets required to launch them are smaller and more cost-effective. However, a drawback of LEO satellites is the need for a larger number to cover a specific geographical area. As LEO satellites orbit the Earth multiple times a day, a continuous chain of satellites is necessary for seamless communication coverage. This complexity extends to the network infrastructure, requiring numerous ground stations and different frequencies to avoid interference.The lower altitude of LEO satellites results in lower latency, crucial for real-time communication like voice calls. MEO satellites, positioned between above LEO, are commonly used for positioning information like GPS. However, they share some challenges such as higher fuel requirements, larger size, and increased communication latency, making them a careful consideration when designing a satellite constellation.


## Source : 
- https://www.wavein.com.tw/
- https://www.qualcomm.com/5g/what-is-5g
- https://www.cisco.com/c/en/us/solutions/what-is-5g.html#~faqs
- https://dgtlinfra.com/explaining-the-key-differences-between-4g-and-5g/
