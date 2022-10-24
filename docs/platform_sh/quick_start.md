---
title: "Quick Start: Deploying to Platform.sh"
hide:
    - footer
---

Quick Start: Deploying to Platform.sh
===

## Overview

Support for Platform.sh is in a very preliminary phase. For example, it may not work when deploying from Windows. It should work if you're using `requirements.txt`, but may not work if you're using Poetry or Pipenv. `django-simple-deploy` should only be used on test projects at this point.

Deployment to Platform.sh can be fully automated, but the configuration-only approach is recommended. This allows you to review the changes that are made to your project before committing them and making the initial push. The fully automated approach configures your project, commits these changes, and pushes the project to Platform.sh' servers.

## Prerequisites

Deployment to Platform.sh requires three things:

- You must be using Git to track your project.
- You need to have a `requirements.txt` file at the root of your project.
- The [Platform.sh CLI](https://docs.platform.sh/development/cli.html) must be installed on your system.

## Configuration-only deployment


First, install `platformshconfig`. This package is used to determine whether local settings or Platform.sh-specific settings should be used:

```
$ pip install platformshconfig
```

Now, install `django-simple-deploy`, and add `simple_deploy` to `INSTALLED_APPS` in *settings.py*:

```
$ pip install django-simple-deploy
# Add "simple_deploy" to INSTALLED_APPS in settings.py.
```

Now create a new Platform.sh app using the CLI, and run `simple_deploy` to configure your app:

```
$ platform create
$ python manage.py simple_deploy --platform platform_sh
```

At this point, you should review the changes that were made to your project. Running `git status` will show you which files were modified, and which new files were created.

If you want to continue with the deployment process, commit these changes and run the `push` command. When deployment is complete, use the `url` command to see the deployed version of your project:

```
$ git add .
$ git commit -m "Configured for deployment to Platform.sh."
$ platform push
$ platform url
```

You can find a record of the deployment process in `simple_deploy_logs`. It contains most of the output you saw when running `simple_deploy`.

## Automated deployment

If you want, you can automate this entire process. This involves just four steps:

```
$ pip install platformshconfig
$ pip install django-simple-deploy
# Add `simple_deploy` to INSTALLED_APPS in settings.py.
$ python manage.py simple_deploy --platform platform_sh --automate-all
```

You should see a bunch of output as Platform.sh resources are created for you, your project is configured for deployment, and `simple_deploy` pushes your project to Platform.sh' servers. When everything's complete, your project should open in a new browser tab.

## Pushing further changes

After the initial deployment, you're almost certainly going to make further changes to your project. When you've updated your project and it works locally, you can commit these changes and push your project again, without using `simple_deploy`:

```
$ git status
$ git add .
$ git commit -m "Updated project."
$ platform push
```

## Troubleshooting

If deployment does not work, please feel free to open an [issue](https://github.com/ehmatthes/django-simple-deploy/issues). Please share the OS you're  using locally, and the specific error message or unexpected behavior you saw. If the project you're deploying is hosted in a public repository, please share that as well.

Please remember that `django-simple-deploy` is in a preliminary state. That said, I'd love to know the specific issues people are running into so we can reach a 1.0 state in a reasonable timeframe.

