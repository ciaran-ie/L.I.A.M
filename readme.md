# L.I.A.M. - Law-Enforcement Investigations and Asset Management

L.I.A.M is a simple Python Flask web application for managing digital forensic cases and digital forensic evidence items. It can use SQLite/SQL as the storage backend, and it is intended to be used as a workflow tool for receiving, booking, note-taking, and possibly reporting findings. It simplifies and helps in case management when dealing with a large (or small!) number of devices submitted for forensic analysis in a lab.
Ideally this might suit a small forensic lab that is too busy for an Excel sheet but doesn't have the budget for a paid tool.
This project can be run from minimal spec hardware using LINUX.
It is aimed at Law Enforcement Digital Forensics Labs.

Project is fully dockerized and can be up and running in a small number of commands.

This project relies heavily on [Kirjuri](https://github.com/AnttiKurittu/kirjuri).

**Note**: This project is designed for operating on an air-gapped network.

## Features
- Case management
- Evidence tracking
- Reporting and analytics
- User authentication and roles

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
