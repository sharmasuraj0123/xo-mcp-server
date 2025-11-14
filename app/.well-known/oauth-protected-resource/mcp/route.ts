import {
	metadataCorsOptionsRequestHandler,
	protectedResourceHandlerClerk,
} from "@clerk/mcp-tools/next";

const handler = protectedResourceHandlerClerk({
	// Specify which OAuth scopes this protected resource supports
	scopes_supported: ["profile", "email", "openid"],
});
const corsHandler = metadataCorsOptionsRequestHandler();

export { handler as GET, corsHandler as OPTIONS };
