# Reinforcement Learning Basic

## Decision Making and Utility Theory
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/RL1.png)

Decision making is the process in which an agent **performs** an **action** or set of actions in an environment.

Maximum Expected Utility: A rational agent chooses actions so as to maximize expected utility, given its knowledge. 

$$
EU(a) = \sum_{s'} Pr(s') U(s')
$$

To maximize EU, we choose the **best** action 

$$
a^* = \underset{a}{\mathrm{argmax}} \ EU(a)
$$



## Bandit Problem

Tradeoff between **exploration** and **exploitation** is a key to **optimize** decision making for choosing an actions.

**Exploitation** refers to the strategy of using the **knowledge** that the agent **has already gained** to make decisions that yield immediate rewards. When an agent exploits, it chooses actions that it believes will yield the highest reward based on the current information. This is akin to playing it safe and sticking with what is known to work.

**Exploration**, on the other hand, refers to the strategy of **trying out new actions** to discover their potential rewards, which are not yet known. When an agent explores, it might choose an action that is not guaranteed to yield the highest immediate reward, but it may result in new information that can lead to better decisions in the future. This is like taking a risk to learn more about the environment.

Both strategies are important in reinforcement learning:

* Without **exploitation**, an agent might continue exploring indefinitely and never leverage the information it has to achieve high rewards.
* Without **exploration**, an agent might settle on a suboptimal policy because it never discovered actions that could lead to higher rewards.

Action value is the expected reward of an action:
$$
Q^*(a) = \mathbb{E}[R_t | A_t = a]
$$

Greedy action selection: Select **greedy action** **most of the time**, but with **small probability** $\epsilon$, pick a **random action** to explore instead. 

Example: Supposed we have

- $Q(a_1) = 3$
- $Q(a_2) = -2$
- $Q(a_3) = 5$

with e greedy action selection, $a_3$ will always chosen with probability 1 - $\epsilon$, while $a_1$ and $a_2$ may be chosen each with probability 0.5$\epsilon$. 



## Markov Decision Processes

A **Markov Decision Processes (MDP)** is a mathematical model for a sequential decision problem with uncertainty

Components of MDP:
* State space $S$ and action space $A$.
* Transition function that maps probability from current state to successor state, given action a $T(s, a, s') = Pr(s'|s, a)$.
* Reward function $R(s, a, s')$. 

Utility of a state-action sequence

$$V([s_0, a_0, s_1, a_1,..., a_{T-1}, s_T]) = \sum_{t=0}^{T-1} \gamma^t R(s_t, a_t, s_{t+1})$$

Solving a MDP means finding a policy that mapping from states to actions. 




$( V^\pi: S \rightarrow \mathbb{R})$ is the expected utility of following policy $( \pi)$ starting from a given state.

$$
V^\pi(s) = \mathbb{E} \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, \pi(s_t), s_{t+1} \right], s_0 = s
$$

We can write a recursive definition of the value function: 

$$
V^{\pi}(s) = \sum_{s'} T(s, \pi(s), s') \left[R(s, \pi(s), s') + \gamma V^{\pi}(s')\right]
$$

Bellman optimality equations is used to find **optimal policy** and **optimal value function**. 

$$
V^*(s) = \max_{a} \sum_{s'} T(s, a, s') \left[R(s, a, s') + \gamma V^*(s')\right]
$$

$$
\pi^*(s) = \underset{a}{\mathrm{argmax}} \sum_{s'} T(s, a, s') \left[R(s, a, s') + \gamma V^*(s')\right]
$$


## Dynamic Programming

### Value Iteration

Value iteration is a dynamic programming approach to solving for $V^*$

Given time limited values $V_i(s)$, we can compute $V_{i + 1}(s)$ using bellman equation

$$ V_{i+1}(s) = \max_a \sum_{s'} T(s, a, s')[R(s, a, s') + \gamma V_i(s')] $$

**algorithm:**
* Initialize $V_0$ for all state
* Loop from $i = 0$
* For each state s
  $$V_{i+1}(s) = \max_a \sum_{s'} T(s, a, s')[R(s, a, s') + \gamma V_i(s')] $$
* until
$$\max| V_{i+1}(s) - V_i(s) \| < \epsilon$$

### Policy Iteration

A policy can be computed at any point during value iteration which lead to better values

**algorithm:**
- Initialize $\pi_0(s)$ arbitrarily for all states \(s\)
- Loop from \(i = 0\):
  - Policy evaluation: Compute $(V^{\pi_i})$ for policy $(\pi_i)$
  - Policy improvement: Given $(V^{\pi_i})$, find new policy $(\pi_{i+1})$
- Until $(\pi_{i+1} = \pi_i)$


## Monte Carlo
 - Dynamic programming required knowledge of environtment model. 
 - Monte Carlo: Generated sampled experience and average them for different states and action. 
 - Idea: $V(s)$ can be estimated by averagin utilitis observer after visiting $S$
 
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/RL2.png)


**Algorithm:**
- Generate episode $E$ following $\pi$: $s_0, a_0, r_1, s_1, ....s_{T-1}, a_{T-1}, r_T$. 
- For first occurrence of each state $s_t \in E$
  
    - $G \leftarrow \sum_{j=0}^{T-1} \gamma^j r_{j+1}$
    - $V^{\pi}(s_t) \leftarrow \left( \text{Count}(s_t) \times V^{\pi}(s_t) + G \right) / \left( \text{Count}(s_t) + 1 \right)$
    - ${Count}(s_t) \leftarrow \text{Count}(s_t) + 1$
    
    
## Time Difference Learning
- Updated estimations from other learned estimations without waiting for a final outcome (end of episode)

**Formula:**
$$Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma Q(s',a') - Q(s,a) \right]$$

### On-Policy: SARSA
 - Learn values of behaviour policy
 - More likely to choose the "safe" path
$$Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma Q(s',a') - Q(s,a) \right]$$

### Off-Policy: Q-Learning
- Learn values of target policy
- More likely to choose the "shorter" path
$$Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma * \max_{a'} Q(s',a') - Q(s,a) \right]$$

![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/RL3.png)

 














