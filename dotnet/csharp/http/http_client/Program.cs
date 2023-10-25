using System;
using System.Net.Http;
using Microsoft.Extensions.Http;
using Polly;
using Polly.Extensions.Http;

namespace HttpTestClient
{
    public class Program
    {
        public static async Task Main(string[] args)
        {
            var retryPolicy = HttpPolicyExtensions
                .HandleTransientHttpError()
                .WaitAndRetryAsync(3, retryAttempt => TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)));

            var socketHandler = new SocketsHttpHandler { PooledConnectionLifetime = TimeSpan.FromMinutes(15) };
            var pollyHandler = new PolicyHttpMessageHandler(retryPolicy)
            {
                InnerHandler = socketHandler,
            };

            var httpClient = new HttpClient(pollyHandler);
            try
            {
                var response = await httpClient.GetAsync("https://www.google.com/adasdsdsa");
                Console.WriteLine($"Response: \n {response}");
            }
            catch(Exception e)
            {
                Console.WriteLine($"Exception: \n {e}");
            }
        }
    }
}

