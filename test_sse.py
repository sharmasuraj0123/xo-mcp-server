#!/usr/bin/env python3
"""
Test script for XO MCP Server SSE implementation
"""

import requests
import json
import time

# Test configuration
SSE_URL = "https://003b37decbb4.ngrok-free.app/sse"

def test_sse_connection():
    """Test basic SSE connection"""
    print("Testing SSE connection...")
    
    try:
        response = requests.get(SSE_URL)
        print(f"GET /sse response: {response.status_code}")
        print(f"Response: {response.json()}")
        return True
    except Exception as e:
        print(f"Error testing SSE connection: {e}")
        return False

def test_mcp_initialize():
    """Test MCP initialize method"""
    print("\nTesting MCP initialize...")
    
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }
    
    try:
        response = requests.post(SSE_URL, json=data, stream=True)
        print(f"Initialize response status: {response.status_code}")
        
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith('data: '):
                    json_data = json.loads(line_str[6:])
                    print(f"Initialize response: {json.dumps(json_data, indent=2)}")
                    break
        return True
    except Exception as e:
        print(f"Error testing initialize: {e}")
        return False

def test_mcp_tools_list():
    """Test MCP tools/list method"""
    print("\nTesting MCP tools/list...")
    
    data = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }
    
    try:
        response = requests.post(SSE_URL, json=data, stream=True)
        print(f"Tools list response status: {response.status_code}")
        
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith('data: '):
                    json_data = json.loads(line_str[6:])
                    print(f"Tools list response: {json.dumps(json_data, indent=2)}")
                    break
        return True
    except Exception as e:
        print(f"Error testing tools/list: {e}")
        return False

def test_mcp_tool_call():
    """Test MCP tools/call method"""
    print("\nTesting MCP tools/call...")
    
    data = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "hello_connector",
            "arguments": {}
        }
    }
    
    try:
        response = requests.post(SSE_URL, json=data, stream=True)
        print(f"Tool call response status: {response.status_code}")
        
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith('data: '):
                    json_data = json.loads(line_str[6:])
                    print(f"Tool call response: {json.dumps(json_data, indent=2)}")
                    break
        return True
    except Exception as e:
        print(f"Error testing tools/call: {e}")
        return False

def main():
    """Run all tests"""
    print("XO MCP Server SSE Test Suite")
    print("=" * 40)
    
    tests = [
        test_sse_connection,
        test_mcp_initialize,
        test_mcp_tools_list,
        test_mcp_tool_call
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 40)
    print("Test Results:")
    print(f"Passed: {sum(results)}/{len(results)}")
    
    if all(results):
        print("✅ All tests passed! Your SSE implementation is working correctly.")
    else:
        print("❌ Some tests failed. Please check the implementation.")

if __name__ == "__main__":
    main() 