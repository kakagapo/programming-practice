Install-Module AzureAD

Connect-AzureAD -TenantId $tenantId
$appName = "TailwindTradersSalesApp"
$appURI = "https://tailwindtraderssalesapp.twtmitt.onmicrosoft.com"
$appHomePageUrl = "http://www.tailwindtraders.com/"
$appReplyURLs = @($appURI, $appHomePageURL, "https://localhost:1234")
if(!($myApp = Get-AzureADApplication -Filter "DisplayName eq '$($appName)'"  -ErrorAction SilentlyContinue))
{
    $myApp = New-AzureADApplication -DisplayName $appName -IdentifierUris $appURI -Homepage $appHomePageUrl -ReplyUrls $appReplyURLs    
}

New-AzureADApplicationPasswordCredential -ObjectId $AdatumDemoApp.ObjectId -CustomKeyIdentifier "Access Key" -EndDate (get-date).AddYears(1)
