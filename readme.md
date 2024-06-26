# L.I.A.M. - Law-Enforcement Investigations and Asset Management System (WORK IN PROGRESS)

L.I.A.M is an open source case management system for digital forensics labs, its a simple Python Flask web application for managing digital forensic cases and digital forensic evidence items. It can use SQLite/SQL as the storage backend, and it is intended to be used as a workflow tool for receiving, booking, note-taking, and possibly reporting findings. It simplifies and helps in case management when dealing with a large (or small!) number of devices submitted for forensic analysis in a lab.
Ideally this might suit a small forensic lab that is too busy for an Excel sheet but doesn't have the budget for a paid tool.
This project can be run from minimal spec hardware using Ubuntu/linux.
Users can add in storage locations for exhibits, note the date seized and what processes where ran on different exhibits.
Produce chain of custody receipts
Produce Case Reports detailing notes and all details of case in a nicely formated PDF
It is aimed at Law Enforcement Digital Forensics Labs, but could be adapted to any number of small digital forensics labs.

Goal is to have Project fully dockerized and can be up and running in a small number of commands.

Easy storage of all data in a simple SQL/SQLITE so that all the information can be easily backed up and taken to other programs if necessary not locked into this program.


**Note**: This project is designed for operating on an air-gapped network. It should not be deployed over the internet

## Features
- Case management
- Evidence tracking
- Reporting and analytics
- User authentication and roles

## TODO
- Add in autofill for certain items like dates/ sizes of media etc..
- produce easy to follow install instuctions
- create wiki for all different aspects of system and how to use
- create a video showing all the different pages and how to use the system
- create a list of icons to prepopulate the exhibit page to show what type of exhibit it is USB/LAptop/Mobile/Cloud evidence etc..
- Case file number should prepopulate creating new case page based on incremental 
- Create a backup page and easy to use instructions for backup of the information
- report genereattion have it produce a nice PDF with the company/dept logo and all the particulars of the case
- tidy up the case details page
- when the user adds notes to a case have it add the timestamp to the notes
- create a chain of custody page for exhibits which clearly shows exhibit movements
- enable and track the audit logging
- add in option of user to upload documents/pdf/docs etc... to a case(dont store in SQL specify a location in the local machine)
- add in option of user to upload pics of exhibits to a case (dont store in SQL specify a location in the local machine)
- make sure all the style packs are availble offline aswell (Put FONT AWESOME IN REPO!)
- in the dashboard dispay more statistics
- enable the login page

## Screenshots

### Search Cases and Exhibits
![Search Cases and Exhibits](./Screenshots/search_LIAM.png)

### Users
![Users](./Screenshots/users_LIAM.png)

### Exhibits
![Exhibits](./Screenshots/exhibits_LIAM.png)

### Case Details
![Case Details](./Screenshots/casedetails_LIAM.png)

### Cases
![Cases](./Screenshots/cases_LIAM.png)

### Dashboard
![Dashboard](./Screenshots/Dashboard_LIAM.png)

## Installation
- Put in full install instructions
- Reccomend Ubuntu
- DOCKERISE!!!!!!
- HAVE IT RUN ON A RASPBERY PI
## Workflow of ProjectL.I.A.M.

```mermaid
graph TD
    A[Case Creation] --> B[Enter Exhibits]
    B --> C[Assign Tasks]
    C --> D[Evidence Tracking]
    D --> E[Note-taking]
    E --> F[Analysis & Findings]
    F --> G[Report Generation]
    G --> H[Case Review & Closure]
    
    subgraph Workflow
        direction LR
        A --> B --> C --> D --> E --> F --> G --> H
    end
    
    subgraph Additional Features
        B --> I[User Authentication & Roles]
        D --> J[Reporting & Analytics]
        H --> K[Archiving]
    end
