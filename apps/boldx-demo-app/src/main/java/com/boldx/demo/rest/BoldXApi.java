package com.boldx.demo.rest;

import javax.inject.Inject;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import org.jboss.logging.Logger;
import io.micrometer.core.instrument.MeterRegistry;


@Path("/api")
public class BoldXApi {

    private static final Logger LOG = Logger.getLogger(BoldXApi.class);

    @Inject
    MeterRegistry registry;


    @Path("/hello")
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public Response hello() {
        registry.counter("boldx_greeting_counter").increment();
        LOG.info("hello");
        return Response.ok("Hello").build();
    }

    @Path("/bad-request")
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public Response bad_request() {
        registry.counter("boldx_bad_request").increment();
        LOG.warn("bad-request");
        return Response.status(400, "Bad request").build();
    }

    @Path("/unauthorized")
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public Response unauthorized() {
        registry.counter("boldx_unauthorized").increment();
        LOG.error("unauthorized");
        return Response.status(401, "unauthorized").build();
    }

    @Path("/forbidden")
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public Response forbidden() {
        registry.counter("boldx_forbidden").increment();
        LOG.error("forbidden");
        return Response.status(403, "forbidden").build();
    }

    @Path("/not-found")
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public Response not_found() {
        registry.counter("boldx_not_found").increment();
        LOG.warn("not-found");
        return Response.status(404, "not found").build();
    }

    @Path("/error")
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public Response error() {
        registry.counter("boldx_internal_server_error").increment();
        LOG.error("internal-server-error");
        return Response.status(500, "internal-server-error").build();
    }
}
