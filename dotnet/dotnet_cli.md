# dotnet Command line

## To get help

dotnet --help -> this will list the sub-commands supported
dotnet new --help -> to get help related to a sub-command, for example, the new sub-command

## To create new solution

dotnet new sln --name MySolution

## To add new project

dotnet new classlib --framework "netstandard2.0" -o MyLibrary
dotnet new console --language "F#"
dotnet new xunit
`dotnet new mvc -au None` -> authentication mechanism is set to none.

## To add/remove packages

`dotnet add package Microsoft.EntityFrameworkCore`
`dotnet remove package Microsoft.EntityFrameworkCore`

## Note

You don't have to run `dotnet restore` as it is run implicitly when required.

## References:

[dotnet command](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet)