# Reinforcement Learning (RL)
## Reference:
1. [Coursera: Reinforcement Learning Specialization - University of Alberta](https://www.coursera.org/programs/faculty-program-qaslr/specializations/reinforcement-learning) 
2. [Reinforcement Learning An Introduction second edition by Richard S.](https://d3c33hcgiwev3.cloudfront.net/Ph9QFZnEEemRfw7JJ0OZYA_808e8e7d9a544e1eb31ad11069d45dc4_RLbook2018.pdf?Expires=1711065600&Signature=acE3T19e2QKi6gu7CNwLkEDh2PbkTR8Z20V163Vn4-tVDXviK4G24oYbuIwkFIR~dcZXEgvGcgdBLk8kIuPf-YtWJ3JZqGaJ1quuCMQXKnO2au1NfTqSJCwfNLaYcud6Mxpmk7DU3Nq6EIcgCBI3cn6-wE1WYtEsH5Mo9uBdJdE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

In RL, **the reward** represents the quantity of cans collected by the robot. **The agent** learns by experimenting to maximize the collection of cans.

## K-armed Bandits
-  In the k-armed bandit problem, an agent selects from k different actions and earns a reward corresponding to the chosen action. 
- ![image](https://hackmd.io/_uploads/r11uO4dRa.png)
- *Image 1. Example of K-armed bandit problem*
- In the examples, determining the optimal action for a doctor requires defining the value associated with each possible action. These values are referred to as **action values**. 
- **action values Function:** 
$$q_*(a) := \mathbb{E}[R_t \mid A_t = a] \; \forall a \in \{1,2,..,k\}$$
$$= \sum_r p(r|a)r$$
	- := meaning is *defined as* 
	- $q *(a)$ is defined as the expectation of $R_t$, given we selected action A, for each possible action one through k. The value $q_*(a)$ is the reward.
	- The goal of the agent is to maximize the expected reward &rarr; $\operatorname{argmax}_{a} q_*(a)$
	- Inside the sum, multiply each possible reward by the probability of observing that reward.
	
- ![image](https://hackmd.io/_uploads/Hy1zu4u0p.png)
- *Image 2. Bernoulli distribution*
