using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(TickPredict.Startup))]
namespace TickPredict
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
