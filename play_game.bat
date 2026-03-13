@echo off
cd /d "%~dp0"
pip install stable-baselines3
python main.py
pause