# Reinforcement Learning (RL)
## Reference:
1. [Coursera: Reinforcement Learning Specialization - University of Alberta](https://www.coursera.org/programs/faculty-program-qaslr/specializations/reinforcement-learning) 
2. [Reinforcement Learning An Introduction second edition by Richard S.](https://d3c33hcgiwev3.cloudfront.net/Ph9QFZnEEemRfw7JJ0OZYA_808e8e7d9a544e1eb31ad11069d45dc4_RLbook2018.pdf?Expires=1711065600&Signature=acE3T19e2QKi6gu7CNwLkEDh2PbkTR8Z20V163Vn4-tVDXviK4G24oYbuIwkFIR~dcZXEgvGcgdBLk8kIuPf-YtWJ3JZqGaJ1quuCMQXKnO2au1NfTqSJCwfNLaYcud6Mxpmk7DU3Nq6EIcgCBI3cn6-wE1WYtEsH5Mo9uBdJdE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

RL	: **the reward** represents the quantity of cans collected by the robot. **The agent** learns by experimenting to maximize the collection of cans.
## Jupyter Notebook Code
- [Code-1](https://github.com/Bintang-Satwika/StudyNotes-Literature/blob/191e3041246b7e9b444a48a8dc628e4a869d820e/RL_UAlberta/W1_Jupyter.ipynb)
## K-armed Bandits
-  In the k-armed bandit problem, an agent selects from k different actions and earns a reward corresponding to the chosen action. 
- ![image](https://hackmd.io/_uploads/r11uO4dRa.png)
	- *Figure 1. Example of K-armed bandit problem*
- In the examples, determining the optimal action for a doctor requires defining the value associated with each possible action. These values are referred to as **action values**. 
### **action values Function:** 
- $$ q_*(a) := \mathbb{E}[R_t \mid A_t = a] \; \forall a \in \{1,2,..,k\}  $$
- $$  q_*(a) = \sum_r p(r|a)r \tag{2.0}$$ 
- := meaning is *defined as* 
- $q_*(a)$ is defined as the expectation of $R_t$, given we selected action A, for each possible action one through k. The value $q_*(a)$ is the expected reward  (true value of action a).
- The goal of the agent is to maximize the expected reward &rarr; $\operatorname{argmax}_{a} q_*(a)$
- Inside the sum, multiply each possible reward by the probability of observing that reward.
	
- ![image](https://hackmd.io/_uploads/Hy1zu4u0p.png)
	- *Figure 2. Bernoulli distribution*
- $q_*(a)$ is not known to agent, just like the doctor doesn't know the effectiveness of each treatment.
### **Sampel-average Method:**
- estimate  $q_*(a)$: $$Q_t(a) := \frac{\text{sum of rewards when } a \text{ taken prior to }t} {\text{number of times } a \text{ taken prior to } t} = \frac{\sum_{i=1}^{t-1}R_i}{t-1} \tag{2.1}$$
**if action A has not yet been taken, set the value to some default like zero**
- ![image](https://hackmd.io/_uploads/BJxUgxhFRa.png)
	- *Figure 3. Example sample-averaged method*
- **sample-averaged** method can be used to estimate action values
- The **greedy action** is the action with the highest value. from Fig.3, the result of greedy action is argmax Q(a) = 0.75 the Y-action)
###  Incremental Update Rule
- ![image](https://hackmd.io/_uploads/rkVNfnYC6.png)
- **Final Formula**: $$Q_{n+1}= Q_n + \frac{1}{n}(R_n-Q_n) \Leftrightarrow \text{NewEstimate = OldEstimate + StepSize[Target − OldEstimate]} \tag{2.2}$$

###  Nonstationary Problem
- ![image](https://hackmd.io/_uploads/HJRCcnYCT.png)
- **Final Formula**:$$ Q_{n+1}=(1- \alpha)^nQ_1+ \sum_{i=1}^{n} \alpha(1-\alpha)^{n-i}R_i \; \textbf{where} \; \alpha \;  \textbf{is step-size} \tag{2.3} $$
 - The equation (2.3) describes how current estimate of value $(Q_{n+1})$ is related to $Q_1$ and all observed rewards. As more data is gathered, the influence of the initial Q goes to zero. The most recent rewards contribute most to current estimate. The **first term** indicates that the impact of $Q_1$ diminishes exponentially over time. The **second term** suggests that rewards from earlier times have exponentially diminishing influence.
### Exploration vs Exploitation
- **Exploration** occrus when agent try new actions to get more accurate estimates of its values, even if they may not seem optimal at first.
- **Exploitation** occurs when the agent takes the action it currently believes is best, hoping it will yield the highest reward.
-  The agent **can’t** do exploration and exploitation at the same time. The Epsilon-Greedy method  chooses between them for balancing.
#### Epsilon-Greedy 
- $$A_t = \left\{ \begin{array}{rl} \operatorname{argmax}_{a} q_*(a) & \text {with probability}\ 1-\epsilon \\ a \text{~} Uniform(\{a_1 ... a_k\}) & \text {with probability}\ \epsilon \end{array}\right. $$
- When Epsilon-Greedy exploits, it chooses the action which maximizes the current value estimate. When Epsilon-Greedy explores, it chooses an action Uniform randomly.
#### Limitiation Optimistic Initial Values
- ![image](https://hackmd.io/_uploads/BJJ-fe410.png)
- **Limited Exploration**: optimistic initial values only drive exploration early in learning, this means agents will not continue exploring after some time.
- **Non-stationary problems**: For example, one of the action values may change after some number of time steps. An agent might become fixated on an action that was initially good but is no longer optimal due to a shift in the environment
- Setting the appropriate initial value can be tricky. We may not know what the optimistic initial value should be.

#### Upper-Confidence Bound (UCB) 
- UCB mixes exploitation and exploration through the use of **confidence intervals**.
- $$ A_t :=  \operatorname{argmax} \left [{Q_t(a)+c \ln{\sqrt{\frac{\ln t}{N_t(a)} } } } \right]$$
- $Q_t(a)$ is exploration part and $\ln{\sqrt{\frac{\ln t}{N_t(a)} } }$ is exploitation part.
- The C parameter as a user-specified parameter that controls the amount of exploration
- ![image](https://hackmd.io/_uploads/H12_Yx4J0.png)

### Notation K-armed Bandits
![image](https://hackmd.io/_uploads/ry5OvddA6.png)
![image](https://hackmd.io/_uploads/ry0FD__Ra.png)


## Markov Decision Processes
![image](https://hackmd.io/_uploads/B1g4xVbeR.png)
![image](https://hackmd.io/_uploads/rJYNWE-eA.png)

![image](https://hackmd.io/_uploads/rkAb-EWlC.png)
 - The function (p) calculates the likelihood of next state (S’) and the associated reward, given state (S) and action (a)
 - Since p is a probability distribution, it must be non-negative and it's sum over all possible next states and rewards must equal one

### Example for recycling robot which collects empty soda cans in an office environment
- ![image](https://hackmd.io/_uploads/Bku8MEbe0.png)
- ![image](https://hackmd.io/_uploads/Bk_qGEbl0.png)
-![image](https://hackmd.io/_uploads/Hkb3GNWxA.png)

- ![image](https://hackmd.io/_uploads/H1DNzV-lC.png)
- **$\alpha$ and $\beta$ is probability**


### Example for a robot arm in a pick-and-place task:
- Goal: The robot arm must pick up objects and place them in a specified location.
- State: Defined by the readings of the joint angles and velocities of the robot arm.
- Actions: Represented by the voltages applied to the motors controlling the arm.
- Reward: The robot receives a reward of +100 for each object successfully placed in the target location. The reward -1 for each unit of energy consumed

### Episodic task
 - the goal of an agent in terms of maximizing the expected return $(G_t)$. The agent environment interaction breaks up into episodes. Each episode begins independently of how the previous one ended.
- At termination, the agent is reset to a start state. Every episode has a final state which call the **terminal state**.
- The number of steps in an episode is stochastic: each episode can have a different number of steps. 
- example episodic: chess game, video games like image below.
- ![image](https://hackmd.io/_uploads/H1DSAEZeR.png)
	- state: an array of pixel values corresponding to the current screen
	- Action: Move Up,down,left, or right.
	-  Reward: +1 whenever collect a treasure block
	- An episode ends when the agent touches one of the green enemies. The next episode begin with the agent in the center of the screen with no enemies present
### Continuing task
- Example continuing task: Sceduler
	- State: priority and free servers
	- Action: accept or reject
	- reward: accepting the job, runs it and yields a reward equal to the jobs priority. Rejecting a job yields a negative reward proportional to the priority, and sends the job to the back of the queue.
- Example continuing task:  smart thermostat which regulates the temperature of a building. since the thermostat never stops interacting with the environment. 
	- State: current temperature, the time of day, and the number of people in the building.
	- Action: turn on the heater or turn it off.
	- Reward : -1 every time someone adjust temperature manually, and 0 otherwise.
- ![image](https://hackmd.io/_uploads/BkhEiEbg0.png)
- ![image](https://hackmd.io/_uploads/S1sjiEZg0.png)
-  factor $\gamma$ called the **discount rate** where $0 \le \gamma < 1$. Immediate rewards contribute more. Rewards far into the future contribute less because multiplied by Gamma raised to successively larger powers of k. **Discounting is used to ensure returns are finite**.
- ![image](https://hackmd.io/_uploads/r16_2NZl0.png)

| Episodic task |Contiuning task |
| --- | --- |
|interaction breaks into episodes|interaction goes continually|
|each episode ends in a terminal state. Episodes are independent|No terminal state|
|$G_t = R_{t+1}+R_{t+2}+...+R_{t}$|$G_t = R_{t+1}+\gamma G_{t+1}$|
||$G_t= \sum_{k=0}^\infty \gamma^k R_{t+k+1}$|

### Notation MDP
- ![image](https://hackmd.io/_uploads/HyXBMB-l0.png)

## Policies and Value Functions
- an agent's behavior is specified by a policy that maps the state to a probability distribution over actions
- **the policy can depend only on the current state**. It can't depend on things like time or previous states. 
-  **state value** function refers to the expected return from a given state under a specific policy. $$V_\pi(s) := \mathbb{E}_\pi [G_t|S_t=s]$$
-  **action value** function refers to the expected return from a given state after selecting a particular action and then following a given policy. $$q_\pi(s,a) := \mathbb{E}_\pi[G_t|S_t=s, A_t=a]$$
### Bellman equation
- ![image](https://hackmd.io/_uploads/rkSJquGeC.png)

- **State-value Bellman**: $$v_{\pi}(s)=\sum_a \pi(a|s) \sum_{s'} \sum_r p(s',r|s,a)[r+\gamma v_\pi(s')]$$
-![image](https://hackmd.io/_uploads/HJX1k5feC.png)
- **Action-Value Bellman** $$ q_\pi(s,a)=\sum_{s'} \sum_r p(s',r|s,a)[r+\gamma \sum \pi (a'|s)q_\pi (s',a')]$$

- Bellman equations provide relationships between the values of a state or state action pair, and the possible next states or next state action pairs.
#### Example :gridworld
- ![image](https://hackmd.io/_uploads/H1nB-9zlA.png)
- with $\gamma=0.7$, the result using linear alegbra are $V_\pi(A)=4.2 , V_\pi(B)=6.1, V_\pi(C)=2.2, V_\pi(D)=4.2$

### Optimal Policy 
- an optimal policy is defined as the policy with the highest value in all states. At least one optimal policy always exists but there may be more than one. 
- Optimal Policy: $$ \pi_1 \geq \pi_2 \text{ if } v_{\pi_1}(s) \geq v_{\pi_2}(s) \text{ for every state}$$
![image](https://hackmd.io/_uploads/SJpq0f7lR.png)
- Optimal State Value Function: $$V_{\pi*}=\max_\pi v_\pi(s) \text{ for every state}$$ 
- optimal action value functions: $$q_\pi*(s,a) := \max_\pi q_\pi(s,a) \text{ for every state and action}$$
- Belmann Equation for Optimal State: $$v_{*}(s)=\max_a \sum_{s'} \sum_r p(s',r|s,a)[r+\gamma v_*(s')]$$
- Belmann Equation for Optimal Action: $$q_*(s,a)=\sum_{s'} \sum_r p(s',r|s,a)[r+\gamma \max_{a'} q_* (s',a')]$$
- Dynamics of the MDP: $$\pi_{*}(s)=\operatorname{argmax}_a \sum_{s'} \sum_r p(s',r|s,a)[r+\gamma v_*(s')]$$
- ![image](https://hackmd.io/_uploads/r1UmOU8e0.png)

### Notation Belmann
- ![image](https://hackmd.io/_uploads/H1Y6N5Ml0.png)
