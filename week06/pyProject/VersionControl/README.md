# MSE800 - Week 06
# Version Control with Git & GitHub

## Overview

This week focused on **Version Control** using **Git** and **GitHub**.

Instead of learning new Python programming concepts, we learned how software developers manage source code, track changes, and collaborate with others using Git.

Version control is an important skill in modern software engineering.

---

# Learning Objectives

After this week, I can:

- Understand the purpose of Version Control.
- Create a Git repository.
- Track file changes.
- Save project history using commits.
- Upload projects to GitHub.
- Synchronize local and remote repositories.
- Resolve simple Git conflicts.
- Organize software projects using Git.

---

# What is Version Control?

Version Control is a system that records changes to files over time.

It allows developers to:

- Keep project history.
- Restore previous versions.
- Work together on the same project.
- Prevent accidental loss of code.

Git is one of the most popular Version Control Systems.

---

# Git vs GitHub

## Git

Git is software installed on a local computer.

It manages project history and tracks file changes.

Examples:

- git init
- git add
- git commit

---

## GitHub

GitHub is an online platform that stores Git repositories.

It allows developers to:

- Share projects
- Backup code
- Collaborate with others

---

# Common Git Commands

## Create Repository

```bash
git init
```

Create a new Git repository.

---

## Check Repository Status

```bash
git status
```

Show modified, staged, and untracked files.

---

## Add Files

```bash
git add .
```

Stage all modified files.

---

## Commit Changes

```bash
git commit -m "Update project"
```

Save a new version of the project.

---

## View Commit History

```bash
git log
```

Display previous commits.

---

## Connect GitHub

```bash
git remote add origin <repository_url>
```

Connect the local repository to GitHub.

---

## Upload Project

```bash
git push origin main
```

Upload commits to GitHub.

---

## Download Latest Changes

```bash
git pull origin main
```

Download updates from GitHub.

---

# Typical Git Workflow

```
Edit Files
      ↓
git status
      ↓
git add .
      ↓
git commit
      ↓
git push
      ↓
GitHub
```

---

# Git Repository Structure

Example:

```
MSE800/
│
├── .git
├── week01
├── week02
├── week03
├── week04
├── week05
├── week06
├── week07
└── README.md
```

Only the **MSE800** folder should contain the `.git` directory.

Subfolders (Week01, Week02, etc.) should not be initialized as separate Git repositories.

---

# Common Git Problems

## Accidentally Running git init

If a subfolder is initialized with:

```bash
git init
```

it creates another `.git` directory.

This results in a nested Git repository.

Solution:

```bash
rm -rf .git
```

Delete the unnecessary `.git` folder inside the subfolder.

---

## Push Rejected

Example:

```
non-fast-forward
```

Solution:

```bash
git pull origin main
git push origin main
```

---

## Merge Commit Message

When Git opens the editor:

```
Merge branch 'main'
```

Save and exit.

For Vim:

```
ESC
:wq
```

---

# Why Version Control is Important

Version Control helps developers:

- Save project history.
- Recover previous versions.
- Collaborate with team members.
- Track software development.
- Manage large projects.

Almost every software company uses Git.

---

# My Learning Summary

This week, I learned the basic workflow of Git and GitHub.

I understand how to:

- initialize a repository,
- commit project changes,
- push code to GitHub,
- pull updates,
- and organize projects using a single Git repository.

These skills will be useful for future software engineering projects and team collaboration.

---

# Key Vocabulary

| Word | Meaning |
|------|---------|
| Version Control | 版本控制 |
| Repository | 仓库 |
| Commit | 提交 |
| Branch | 分支 |
| Merge | 合并 |
| Clone | 克隆 |
| Push | 上传到 GitHub |
| Pull | 下载最新代码 |
| Remote | 远程仓库 |
| Local | 本地仓库 |
| Conflict | 冲突 |
| Stage | 暂存 |
| History | 历史记录 |

---

# Reflection

Before this week, I only used GitHub to store my code.

After learning Version Control, I understand that Git is more than cloud storage. It records the development history of a project and makes collaboration much easier.

I will continue using Git to manage all my MSE800 projects.