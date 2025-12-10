import { verifyClerkToken } from "@clerk/mcp-tools/next";
import { createMcpHandler, withMcpAuth } from "@vercel/mcp-adapter";
import { auth, clerkClient } from "@clerk/nextjs/server";

const clerk = await clerkClient();

const handler = createMcpHandler((server) => {
	// server.tool(
	// 	"get-clerk-user-data",
	// 	"Gets data about the Clerk user that authorized this request",
	// 	{},
	// 	async (_, { authInfo }) => {
	// 		const userId = authInfo!.extra!.userId! as string;
	// 		const userData = await clerk.users.getUser(userId);

	// 		return {
	// 			content: [{ type: "text", text: JSON.stringify(userData) }],
	// 		};
	// 	}
	// );

	server.tool(
		"fetch",
		"A simple fetch tool that says hello",
		{},
		async () => {
			return {
				content: [{ type: "text", text: "Hi I am fetch" }],
			};
		}
	);

	server.tool(
		"search",
		"A simple search tool that identifies itself",
		{},
		async () => {
			return {
				content: [{ type: "text", text: "Hi I am search" }],
			};
		}
	);
});

const authHandler = withMcpAuth(
	handler,
	async (_, token) => {
		const clerkAuth = await auth({ acceptsToken: "oauth_token" });
		return verifyClerkToken(clerkAuth, token);
	},
	{
		required: true,
		resourceMetadataPath: "/.well-known/oauth-protected-resource/mcp",
	}
);

export { authHandler as GET, authHandler as POST };
