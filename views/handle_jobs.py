import random
from flask import render_template
from models.job import Job
from models.game_state import GameState
from services import job_services


def make_stars(count):
    # Unicode star
    return "★" * int(count)


def handle_jobs(bot, chat_dest):
    game_state = GameState.load_from_dynamodb(chat_dest)
    # Get job for the user
    jobs = Job.load_jobs_from_file('data/jobs.yaml')
    jobs_for_user = job_services.filter_jobs_by_skills(
        jobs, game_state.skill_levels)
    # # Calculate the probability of being accepted for the each job
    # for job in jobs_for_user:
    #     job.acceptance_probability = job_services.calculate_job_acceptance_probability(
    #         job, game_state.skill_levels)

    # text = render_template('jobs.txt', jobs_for_user=jobs_for_user)
    # bot.send_message(chat_dest, text)
