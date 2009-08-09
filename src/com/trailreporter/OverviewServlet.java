package com.trailreporter;

import java.io.IOException;
import javax.servlet.http.*;
import com.google.appengine.api.users.User;
import com.google.appengine.api.users.UserService;
import com.google.appengine.api.users.UserServiceFactory;

/**
 * A servlet to display the main page.
 */
public class OverviewServlet extends HttpServlet {

    /**
     * Handles a GET request.
     * @param req
     * @param resp
     * @throws IOException
     */
    public void doGet(HttpServletRequest req, HttpServletResponse resp)
        throws IOException {

        UserService userService = UserServiceFactory.getUserService();
        User user = userService.getCurrentUser();

        if (user != null) {
            resp.setContentType("text/plain");
            resp.getWriter().println("Hello, " + user.getNickname());
        } else {
            resp.sendRedirect(userService.createLoginURL(req.getRequestURI()));
        }
    }
}

/* EOF */
