import React from 'react';
import { Navigate } from 'react-router-dom';
import MainLayout from 'src/layouts/MainLayout';
import DashboardView from 'src/views/DashboardView';
import ProjectDescriptionView from 'src/views/ProjectDescriptionView';
import TeamView from 'src/views/TeamView';

const routes = [
  {
    path: '/',
    element: <MainLayout />,
    children: [
      { path: '/', element: <Navigate to="/dashboard" /> },
      { path: 'dashboard', element: <DashboardView /> },
      { path: 'projectdescription', element: <ProjectDescriptionView /> },
      { path: 'team', element: <TeamView /> },
      { path: '*', element: <Navigate to="/404" /> }
    ]
  }
];

export default routes;
