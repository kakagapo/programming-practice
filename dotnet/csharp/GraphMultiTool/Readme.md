# Graph Multi-Tool

Solution created using the ```dotnet``` command.

```
dotnet new sln --name GraphMultiTool
```

Example command to create/remove projects can be found in the following link

[Mastering Visual Studio 2017](https://learning.oreilly.com/library/view/mastering-visual-studio/9781787281905/9bd26f7c-0cad-4b7c-9090-9063816b9dcd.xhtml)

Quick command reference:

To add a project and then add it to the solution

```
pushd src\dev
dotnet new classlib -n "GraphCommon"
dotnet new classlib -n "FileSystemAsGraph"
dotnet new console -n "CommandLine"
popd
dotnet sln GraphMultiTool.sln add src\dev\GraphCommon\GraphCommon.csproj
dotnet sln GraphMultiTool.sln add src\dev\FileSystemAsGraph\FileSystemAsGraph.csproj
dotnet sln GraphMultiTool.sln add src\dev\CommandLine\CommandLine.csproj
```

Currently going with the following folder structure

src\dev -> contains all the code for the tool
src\test\unittest -> unit tests with mocking
src\test\integrationtest -> integration tests
