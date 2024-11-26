![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!




Here are the **User Stories** and **Acceptance Criteria** tailored to your project requirements. Each User Story is defined using the **As a [role], I want [feature], so that [benefit]** format.

---

### **User Story 1: View Restaurant Information**
**Description**: 
As a **visitor**, I want to view information about the restaurant, so that I can learn about its background and offerings.

**Acceptance Criteria**:
- [ ] The homepage (`index.html`) displays a welcoming introduction to the restaurant.
- [ ] The "About Us" page (`about.html`) contains details about the restaurant's history and specialties.
- [ ] Links to other pages are accessible from the navigation bar.

---

### **User Story 2: View Menu**
**Description**: 
As a **visitor**, I want to view the restaurant's menu, so that I can decide what to order.

**Acceptance Criteria**:
- [ ] The "Menu" page (`menu.html`) lists all available menu items with their names, descriptions, and prices.
- [ ] Menu data is dynamically loaded from the database.
- [ ] The menu page is responsive and accessible on both desktop and mobile devices.

---

### **User Story 3: Make a Reservation**
**Description**: 
As a **customer**, I want to book a table for a specific date and time, so that I can secure a spot at the restaurant.

**Acceptance Criteria**:
- [ ] The "Reservation" page (`reservation.html`) has a form to input date, time, number of people, and contact information.
- [ ] The system validates that the table is available for the chosen date and time.
- [ ] Customers receive a confirmation message upon successful booking.
- [ ] If a table is unavailable, customers see a message prompting them to choose another time.

---

### **User Story 4: Avoid Double Bookings**
**Description**: 
As a **restaurant manager**, I want to ensure that tables are not double-booked, so that customers have a guaranteed spot.

**Acceptance Criteria**:
- [ ] The system prevents duplicate reservations for the same table and time.
- [ ] Only available tables are shown for booking.

---

### **User Story 5: Manage Reservations**
**Description**: 
As a **customer**, I want to view, edit, or cancel my reservation, so that I can make changes if my plans change.

**Acceptance Criteria**:
- [ ] Customers can access their reservation details using their contact information.
- [ ] Customers can update their reservation's date, time, or party size.
- [ ] Customers can cancel a reservation with a confirmation modal.
- [ ] A success or error message is displayed after editing or canceling.

---

### **User Story 6: Contact the Restaurant**
**Description**: 
As a **visitor**, I want to send a message to the restaurant, so that I can ask questions or provide feedback.

**Acceptance Criteria**:
- [ ] The "Contact" page (`contact.html`) contains a form for entering a name, email, and message.
- [ ] The system sends an email to the restaurant's inbox upon form submission.
- [ ] A modal appears to confirm successful message delivery.

---

### **User Story 7: Authentication for Reservation Management**
**Description**: 
As a **customer**, I want to log in to manage my reservations, so that my information is secure.

**Acceptance Criteria**:
- [ ] Customers can create an account and log in to the system.
- [ ] Only logged-in users can view, edit, or cancel their reservations.
- [ ] The system ensures secure password storage and authentication.

---

### **User Story 8: Admin Menu Management**
**Description**: 
As a **restaurant manager**, I want to add, edit, or delete menu items, so that I can keep the menu up-to-date.

**Acceptance Criteria**:
- [ ] Admin users can log in to the Django admin panel.
- [ ] Menu items can be added, edited, or deleted from the database via the admin panel.
- [ ] Changes to the menu are immediately reflected on the website.

---

### **User Story 9: Deployment and Scalability**
**Description**: 
As a **developer**, I want the project to be deployed to Heroku with a PostgreSQL database, so that it is accessible online and scalable.

**Acceptance Criteria**:
- [ ] The project uses SQLite during development and PostgreSQL in production.
- [ ] Environment variables (e.g., `DATABASE_URL`) are properly configured for Heroku deployment.
- [ ] The application is accessible via a public URL provided by Heroku.

---

### **User Story 10: Responsive Design**
**Description**: 
As a **visitor**, I want the website to be fully responsive, so that I can access it on any device.

**Acceptance Criteria**:
- [ ] All pages are optimized for desktop, tablet, and mobile views.
- [ ] Bootstrap is used for responsive layout design.
- [ ] Navigation and modals function correctly across devices.






