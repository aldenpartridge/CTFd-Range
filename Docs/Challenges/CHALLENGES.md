# CTFd Challenges Documentation

## Overview

Challenges are the main form of content in CTFd. Most functionality in CTFd is centered around challenges and how users interact with them.

Primarily, when users interact with challenges, they can submit a flag (a.k.a. an answer) to the challenge and CTFd will reward the user with points.

---

## Files

Some CTF challenges require supporting files. CTFd allows users to upload files to be displayed and downloaded along with the challenge.

Any user that can view a challenge, can download the files associated with the challenge.

---

## Flags

In most CTFs, the objective is to extract a flag value from a challenge. Often by exploiting some kind of security vulnerability or by knowing some property of computers. Flags are sort of the proof that you accomplished the task.

In order for a user to receive points for a challenge, they must submit the corresponding flag. CTFd allows admins to create different types of flags for each challenge.

A breakdown of the different flag types available in CTFd can be found in the Flags section.

---

## Hints

CTFd allows admins to create hints which can be unlocked by users.

Hints can either be free or have an associated cost with them. Users that unlock paid hints receive a drop in their score equal to the cost of the hint. For example, if a challenge has a hint that costs 50 points, a user must have at least a score of 50 to unlock the hint. More concretely, if a user has 300 points, then unlocks a hint that costs 50 points, the user will then have a score of 250.

If a user does not have enough points to unlock a hint, they will be unable to unlock a hint. A user is unable to lower their score beyond zero to unlock a hint. Because of this one recommended approach to having paid hints is to create an intial "gimme" challenge that will give the user some free points to then subsequently unlock hints in later challenges.

### CAUTION

Keep in mind that in many online CTFs, users can create unlimited accounts. So having paid hints may not be a reliable mechanism for point deduction as users may create throwaway accounts to unlock hints and then use the hint knowledge on their "main" account.

---

## Next Challenge

CTFd provides an option for admins to recommend the next challenge to solve after a user solves one.

Users can skip this one by clicking on the "x" button on the top right. However, if you want to prevent users from accessing challenges other than the challenge specified on the Next Challenge, you can use Requirements to hide or anonymize other challenges before they solve the required challenges.

---

## Requirements

CTFd supports challenges that cannot be seen/interacted with until a prerequisite challenge has been solved.

Challenge requirements can be used to create trees of challenges that users must go through to accomplish everything.

Admins can also choose whether to anonymize the challenge if it hasn't been unlocked or to hide the challenge completely.

---

## Tags

Tags are simple small text strings that can be used to categorize challenges. They are visible to users when viewing challenges.

In addition, some themes will apply a special CSS class to challenges based on the tag. By using this functionality, challenges can be slightly themed by using the tag.

---

## Topics

Topics are small text strings that can be used to explain what topics a challenge requires. They are only visible to admins in the Admin Panel.

A good way to make use of Topics is to keep them in a `challenge.yml` file for ctfcli so that it's clear what topics a given challenge covers.

---

*Last Updated: 2025*
