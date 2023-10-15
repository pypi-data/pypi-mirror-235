use std::cell::Cell;

use crate::AgentId;

pub const REWARD_GEM_COLLECTED: i32 = 1;
pub const REWARD_AGENT_DIED: i32 = -1;
pub const REWARD_AGENT_JUST_ARRIVED: i32 = 1;
pub const REWARD_END_GAME: i32 = 1;

pub trait RewardCollector {
    fn notify(&self, event: RewardEvent);
}

// pub struct IndependentRewardCollector {
//     agent_rewards: RefCell<Vec<i32>>,
// }

// impl IndependentRewardCollector {
//     pub fn new(n_agents: usize) -> Self {
//         Self {
//             agent_rewards: RefCell::new(vec![0; n_agents]),
//         }
//     }
// }

// impl RewardModel<Vec<i32>> for IndependentRewardCollector {
//     fn notify(&self, event: RewardEvent) {
//         let mut agent_rewards = self.agent_rewards.borrow_mut();
//         match event {
//             RewardEvent::JustArrived { agent_id } => {
//                 agent_rewards[agent_id] += REWARD_AGENT_JUST_ARRIVED;
//             }
//             RewardEvent::GemCollected { agent_id } => {
//                 agent_rewards[agent_id] += REWARD_GEM_COLLECTED;
//             }
//             RewardEvent::AgentDied { agent_id } => {
//                 agent_rewards[agent_id] += REWARD_AGENT_DIED;
//             }
//         }
//     }

//     // fn consume(&self) -> Vec<i32> {
//     //     self.agent_rewards.take()
//     // }

//     fn reset(&self) {
//         self.agent_rewards.take();
//     }
// }

#[derive(Debug)]
pub struct SharedRewardCollector {
    step_reward: Cell<i32>,
    n_dead: Cell<u32>,
    episode_gems_collected: Cell<u32>,
    episode_agents_arrived: Cell<u32>,
    n_agents: u32,
}

#[derive(PartialEq, Clone)]
pub enum RewardEvent {
    JustArrived { agent_id: AgentId },
    GemCollected { agent_id: AgentId },
    AgentDied { agent_id: AgentId },
}

impl SharedRewardCollector {
    pub fn new(n_agents: u32) -> Self {
        Self {
            step_reward: Cell::new(0),
            n_dead: Cell::new(0),
            episode_gems_collected: Cell::new(0),
            episode_agents_arrived: Cell::new(0),
            n_agents,
        }
    }

    pub fn notify(&self, event: RewardEvent) {
        // If the agent has died,
        if let RewardEvent::AgentDied { .. } = &event {
            // increase the number of dead agents,
            self.n_dead.set(self.n_dead.get() + 1);
            // cap the current reward to 0,
            let r = self.step_reward.get().min(0);
            // and add the reward for the agent dying.
            self.step_reward.set(r + REWARD_AGENT_DIED);
            return;
        }

        // Otherwise, if an agent has already died, we don't give any positive reward.
        if self.n_dead.get() > 0 {
            return;
        }

        // Last (general) case: all agents are alive
        let event_reward = match event {
            RewardEvent::JustArrived { .. } => {
                self.episode_agents_arrived
                    .set(self.episode_agents_arrived.get() + 1);
                if self.episode_agents_arrived() == self.n_agents {
                    REWARD_AGENT_JUST_ARRIVED + REWARD_END_GAME
                } else {
                    REWARD_AGENT_JUST_ARRIVED
                }
            }
            RewardEvent::GemCollected { .. } => {
                self.episode_gems_collected
                    .set(self.episode_gems_collected.get() + 1);
                REWARD_GEM_COLLECTED
            }
            RewardEvent::AgentDied { .. } => unreachable!(),
        };
        self.step_reward.set(self.step_reward.get() + event_reward);
    }

    /// Reset the reward collector and return the reward for the step.
    pub fn consume_step_reward(&self) -> i32 {
        let n_deads = self.n_dead.get();
        let reward = self.step_reward.get();

        self.n_dead.set(0);
        self.step_reward.set(0);

        if n_deads > 0 {
            return -(n_deads as i32);
        }
        reward
    }

    pub fn episode_gems_collected(&self) -> u32 {
        self.episode_gems_collected.get()
    }

    pub fn episode_agents_arrived(&self) -> u32 {
        self.episode_agents_arrived.get()
    }

    pub fn reset(&self) {
        self.n_dead.set(0);
        self.step_reward.set(0);
        self.episode_agents_arrived.set(0);
        self.episode_gems_collected.set(0);
    }
}

impl Clone for SharedRewardCollector {
    fn clone(&self) -> Self {
        Self {
            step_reward: Cell::new(self.step_reward.get()),
            n_dead: Cell::new(self.n_dead.get()),
            episode_gems_collected: Cell::new(self.episode_gems_collected.get()),
            episode_agents_arrived: Cell::new(self.episode_agents_arrived.get()),
            n_agents: self.n_agents,
        }
    }
}
