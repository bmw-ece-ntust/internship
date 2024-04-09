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

$$
V([\mathbf{s}_0, a_0, \mathbf{s}_1, a_1, \ldots, a_{T-1}, \mathbf{s}_T]) = \sum_{t=0}^{T-1} \gamma^t R(\mathbf{s}_t, a_t, \mathbf{s}_{t+1})
$$

Solving a MDP means finding a policy that mapping from states to actions. 




$( V^\pi: S \rightarrow \mathbb{R})$ is the expected utility of following policy $( \pi)$ starting from a given state.

$$
V^\pi(s) = \mathbb{E} \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, \pi(s_t), s_{t+1} \right], s_0 = s
$$

We can write a recursive definition of the value function: 

$$
V^{\pi}(s) = \sum_{s'} T(s, \pi(s), s') \left[R(s, \pi(s), s') + \gamma V^{\pi}(s')\right]
$$

Bellman optimality equations are used to find optimal policy and optimal value function.

$$
V(s) = \max_a \sum_{s'} T(s, a, s') \left[R(s, a, s') + \gamma V(s')\right]
$$

$$
\pi(s) = \arg\max_a \sum_{s'} T(s, a, s') \left[R(s, a, s') + \gamma V(s')\right]
$$














