package main

import (
	"context"
	"encoding/json"
	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"log"
)

func HandleRequest(ctx context.Context, request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	log.Println(" * DEBUG: Hello world!")

	eventJson, _ := json.Marshal(request)
	log.Printf(" * EVENT: %s", eventJson)

	return events.APIGatewayProxyResponse{Body: string(eventJson), StatusCode: 200}, nil
}

func main() {
	lambda.Start(HandleRequest)
}
