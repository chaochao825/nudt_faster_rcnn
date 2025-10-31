import torch
import os
from attacks.attacks import FasterRCNNAttacks

def main(args, cfg):
    """Main entry point for Faster R-CNN detector"""
    
    if cfg.mode == 'adv':
        # Generate adversarial samples
        attacker = FasterRCNNAttacks(cfg)
        attacker.run_adv(args)
    elif cfg.mode == 'attack':
        # Evaluate model under attack
        attacker = FasterRCNNAttacks(cfg)
        attacker.run_attack(args)
    elif cfg.mode == 'defend':
        # Apply defense mechanisms
        from defends.defends import FasterRCNNDefends
        defender = FasterRCNNDefends(cfg)
        defender.run_defend(args)
    elif cfg.mode == 'train':
        # Train the model
        from train.trainer import FasterRCNNTrainer
        trainer = FasterRCNNTrainer(cfg)
        trainer.train()
    else:
        raise ValueError(f"Unknown mode: {cfg.mode}")


