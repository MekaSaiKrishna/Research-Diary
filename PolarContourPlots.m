%% Example: Creating a contour plot using polar coordinates

% make a rectangular grid of r and theta,
% then define x and y in the usual way 
rr = 15:1:20;
thth = (0:.01:1)*2*pi;
[r th] = meshgrid(rr,thth);

x = r.*cos(th);
y = r.*sin(th);

z =x.*y;


figure()

% Creates the filled contour plot
[C,h] = contourf(x,y,z);

% Erases isolines
set(h,'LineColor','none')

% Displays the colorbar with values
colorbar

% Chooses the "jet" color palette for colors
colormap("jet")

% Makes the aspect ratio of plot 1:1
axis equal
