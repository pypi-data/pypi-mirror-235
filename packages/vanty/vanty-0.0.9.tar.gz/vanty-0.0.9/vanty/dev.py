from __future__ import annotations

import subprocess
import sys
from subprocess import run
from typing import Optional

import typer
from honcho.manager import Manager
from rich import print
from typer import Typer

from vanty.config import config

app = Typer(
    name="dev",
    help="Development commands for initializing the project,"
    " running the app, run migrations, etc.",
    no_args_is_help=True,
)


@app.command()
def docs():
    """Open the docs in browser"""
    print("[green] Opening Vanty's docs")
    typer.launch("https://www.advantch.com/docs")


@app.command()
def init():
    """Builds the docker stack"""
    try:
        run(["docker-compose", "build"])
        run(["pnpm", "install"])
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise e


@app.command()
def build_container(container: str):
    """Rebuilds a docker container"""
    try:
        run(["docker-compose", "build", container])
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise e


@app.command()
def start(docker: bool = False):
    """
    Starts the docker stack.
    Uses honcho to run the separate processes.
    Runs:
    - docker-compose up
    - vite dev port 5173
    - vite ssr port 13714
    """
    print("[green] Starting the app...")
    manager = Manager()
    try:
        manager.add_process("docker stack", "docker-compose up")
        # v14.0 issue, with running vite in docker
        manager.add_process("vite dev", "pnpm run dev")
        if config.get("ssr_enabled", False):
            manager.add_process("vite ssr", "node ./assets/frontend/server.js")
        manager.loop()
        sys.exit(manager.returncode)
    except KeyboardInterrupt:
        print("Stopping the app...")
    except subprocess.CalledProcessError as e:
        print(e)


@app.command()
def migrate(options: Optional[str] = None):
    """
    Runs migrations in docker
    Assumes you are running the project in docker containers.
    Accepts options, e.g. --fake-initial.
    """
    commands = [
        "docker-compose",
        "run",
        "--rm",
        "django",
        "python",
        "manage.py",
        "migrate",
    ]
    if options:
        # parse options
        options = options.split(" ")
        commands += options
    try:
        run(commands)
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise e


@app.command()
def make_migrations(options: Optional[str] = None):
    """
    Create migrations.
    Assumes you are running the project in docker containers.
    """
    commands = [
                "docker-compose",
                "run",
                "--rm",
                "django",
                "python",
                "manage.py",
                "makemigrations",
            ]
    
    if options:
        # parse options
        options = options.split(" ")
        commands += options
    try:
        run(commands)
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise e


@app.command()
def create_superuser():
    """
    Creates a verified superuser.
    This extends the default django command to create a verified superuser.
    """
    email = typer.prompt("What is the email of the superuser?")
    try:
        run(
            [
                "docker-compose",
                "run",
                "--rm",
                "django",
                "python",
                "manage.py",
                "create_verified_superuser",
                email,
            ]
        )
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise e


@app.command()
def stripe_cli():
    print("[green] Opening Stripe CLI")
    # check if stripe cli is installed
    try:
        run(["stripe", "version"])
    except FileNotFoundError:
        print("[red] Stripe CLI is not installed. Please install it first.")
        print("[yellow] https://stripe.com/docs/stripe-cli#install")
        return
    commands = [
        "stripe",
        "listen",
        "--forward-to",
        "http://localhost:8080/billing/webhooks/",
    ]
    run(commands)


@app.command()
def run_tests(app_name: str = None, file_name: str = None):
    """
    Runs tests for a specific Django app and file.
    """
    if file_name and file_name.endswith(".py"):
        file_name = file_name[:-3]
    try:
        subprocess.run(
            [
                "docker-compose",
                "run",
                "--rm",
                "django",
                "python",
                "manage.py",
                "pytest",
                f"apps/{app_name}/tests/{file_name}.py",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise e
