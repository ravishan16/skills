# Worker tenant-routing snippet

Use this pattern when sketching edge middleware for auth, tenant routing, and branding.

## Responsibilities

1. Read the incoming hostname.
2. Resolve hostname to tenant metadata from KV or another lightweight control-plane store.
3. Verify the user's Supabase JWT.
4. Derive the allowed tenant scope from the verified token and route context.
5. Permit only the reports or data surfaces that belong to that tenant.
6. Inject tenant branding tokens into the HTML response or config payload.

## Pseudocode outline

```ts
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const hostname = url.hostname;

    const tenantConfig = await env.TENANT_BRANDING.get(hostname, "json");
    if (!tenantConfig) {
      return new Response("Unknown tenant hostname", { status: 404 });
    }

    const jwt = extractBearerToken(request);
    const claims = await verifySupabaseJwt(jwt, env);
    if (!claims || claims.tenant_id !== tenantConfig.tenantId) {
      return new Response("Forbidden", { status: 403 });
    }

    return renderTenantResponse(request, tenantConfig, claims);
  },
};
```

## Notes

- Keep token verification in a trusted layer.
- Keep branding data separate from raw dataset storage.
- Prefer explicit tenant config objects over inferred host naming rules.
