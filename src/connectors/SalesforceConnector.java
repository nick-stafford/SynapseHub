package com.synapsehub.connectors;

import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;
import java.util.Map;
import java.util.HashMap;
import com.google.gson.Gson;

/**
 * SynapseHub Salesforce Connector
 * Handles authentication and data sync with Salesforce REST API
 */
public class SalesforceConnector implements Connector {

    private final String instanceUrl;
    private final String accessToken;
    private final HttpClient httpClient;
    private final Gson gson;

    public SalesforceConnector(String instanceUrl, String accessToken) {
        this.instanceUrl = instanceUrl;
        this.accessToken = accessToken;
        this.httpClient = HttpClient.newHttpClient();
        this.gson = new Gson();
    }

    @Override
    public Map<String, Object> fetchRecord(String objectType, String recordId) throws Exception {
        String endpoint = String.format("%s/services/data/v58.0/sobjects/%s/%s",
            instanceUrl, objectType, recordId);

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(endpoint))
            .header("Authorization", "Bearer " + accessToken)
            .header("Content-Type", "application/json")
            .GET()
            .build();

        HttpResponse<String> response = httpClient.send(request,
            HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) {
            throw new RuntimeException("Salesforce API error: " + response.statusCode());
        }

        return gson.fromJson(response.body(), Map.class);
    }

    @Override
    public String createRecord(String objectType, Map<String, Object> data) throws Exception {
        String endpoint = String.format("%s/services/data/v58.0/sobjects/%s",
            instanceUrl, objectType);

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(endpoint))
            .header("Authorization", "Bearer " + accessToken)
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(gson.toJson(data)))
            .build();

        HttpResponse<String> response = httpClient.send(request,
            HttpResponse.BodyHandlers.ofString());

        Map<String, Object> result = gson.fromJson(response.body(), Map.class);
        return (String) result.get("id");
    }

    @Override
    public void updateRecord(String objectType, String recordId, Map<String, Object> data) throws Exception {
        String endpoint = String.format("%s/services/data/v58.0/sobjects/%s/%s",
            instanceUrl, objectType, recordId);

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(endpoint))
            .header("Authorization", "Bearer " + accessToken)
            .header("Content-Type", "application/json")
            .method("PATCH", HttpRequest.BodyPublishers.ofString(gson.toJson(data)))
            .build();

        httpClient.send(request, HttpResponse.BodyHandlers.ofString());
    }

    @Override
    public String getConnectorName() {
        return "Salesforce";
    }
}
