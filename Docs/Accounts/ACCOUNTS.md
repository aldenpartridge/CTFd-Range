# CTFd Accounts Documentation

## User Mode

### What are User Modes

CTFd has two kinds of "user modes", User Mode and Team Mode. User modes dictate how players register for the competition and how they're scored.

### Team Mode

If you set your CTF to Team Mode, every team will need to choose a captain. Their captain should register a team and then share the team password with their teammates. Their teammates will then be able to use the team name and password to join the team.

All solves, submissions, awards, and hints gotten by a team member will be attributed the team as well as the individual user. To use a metaphor, in basketball when someone scores points the team gets the points, but we still record how many points the player has gotten for the team. The same is true in CTFd.

#### Important Notes:

- Under team mode everyone should register for their own user account. Then one person from each team (the captain) should register a team account and share the team name and password with their fellow teammates. The other members should then join the team using those credentials.

- Solo individuals can still play in Team Mode but they will still need to register a team.

### User Mode

Under User mode, CTFd lets participants play on their own using their user account. Multiple players also share the same account to play together but solves and submissions will all be attributed to the same account instead of broken down by player.

---

## Users

In CTFd, every participant must register for an account before being able to access the CTF challenges. Users can manually register by going to the Registration page if it's available, or admins can manually create users from the Admin Panel or the API.

### Types

There are two main types of users in CTFd.

#### Admin

Admin users are the administrative users of CTFd and are allowed to access the Admin Panel. From the Admin Panel, admins are allowed to add/edit/delete challenges, add/edit/delete pages, modify configuration, add user accounts, edit user accounts etc. Admin users are also able to access sensitive API endpoints and also make changes for any user or team.

Organizers, challenge developers, and other important users should be made into Admin users so that they can help manage the running CTFd instance.

#### User

A user is a regular CTFd user and only has access to the main site. That is, they are unable to access the Admin Panel or access sensitive API endpoints. They're also only able to make changes for their own user profile. Users who are captain of a team are also the only users that can edit their own team's profile.

Users may create their own accounts via the registration page.

### Properties

All users have a set of properties.

- **User Name** - The user's username identifier
- **Email** - The user's email address
- **Password** - The user's password for logging in
- **Website** - A website, if any, that the user may set in their profile
- **Affiliation** - An affiliation, if any, that the user may set in their profile
- **Country** - A country, if any, that the user may set in their profile

Some properties can only be directly edited by an admin in the Admin Panel:

- **Verified** - Verified users mean that they have confirmed their email address by clicking a link in their email address after registering. Most of the time users will be able to directly verify their email address through the email confirmation workflow. However, admins are able to manually mark users as verified.

- **Hidden** - Hidden users do not appear in the scoreboard and are not visible on any public interface. Their solves are not shown in solve counts, scores are not counted in statistics, and their profiles cannot be directly browsed to.

- **Banned** - Banned users cannot access the site in any capacity. Instead of the actual page, they receive an error page stating that they were banned. Keep in mind that banning is an account level ban. It is not an IP address or hardware based ban.

---

## Teams

CTFd, when configured in Team Mode, all participants will need to be a member of a team before being able to access the CTF challenges.

Teams first need to be created by a team captain. Once the team captain has created the team, they can share the team name and team password with their team members. The team members can then use the team credentials to join the team.

### Properties

All teams have a set of properties.

- **User Name** - The teams's name identifier
- **Email** - The teams's email address (not currently used)
- **Password** - The team password for joining the team
- **Website** - A website, if any, that the team captain may set in the team's profile
- **Affiliation** - An affiliation, if any, that the team captain may set in the team's profile
- **Country** - A country, if any, that the team captain may set in the team's profile

Some properties can only be directly edited by an admin in the Admin Panel:

- **Hidden** - Hidden teams do not appear in the scoreboard and are not visible on any public interface. Their solves are not shown in solve counts, scores are not counted in statistics, and their profiles cannot be directly browsed to.

- **Banned** - Banned teams cannot access the site in any capacity. Instead of the actual page, they receive an error page stating that they were banned. Keep in mind that banning is an account level ban. It is not an IP address or hardware based ban.

---

## Examples

### Add 'Countries' Input in User Registration

This example code snippet is used in modifying user registration input, particularly, it allows you to add a Countries option in the user registration page.

See the linked example documentation for the code implementation details.

---

*Last Updated: 2025*
