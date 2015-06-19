using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.IO;
using System.Threading;

namespace TickPredict.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }

        public ActionResult GetTick() {
            long ticks=DateTime.Now.Ticks;
            ViewBag.Message = ticks;

            return View();
        }

        public ActionResult Upload(HttpPostedFileBase file, int delay) {
            long ticks = DateTime.Now.Ticks;
            string uploadname = file.FileName;
            string filepath = Path.Combine(@"C:\TickPredict\Content\",ticks.ToString()+"_"+uploadname);
            if (!System.IO.File.Exists(filepath))
            {
                file.SaveAs(filepath);

                System.Threading.Thread.Sleep(delay);
                System.IO.File.Delete(filepath);
            }
            ViewBag.Message = "###" + ticks.ToString() + "_" + uploadname + "###";
            return View();
        }

        public ActionResult TestTick(string guess)
        {
            long ticks = DateTime.Now.Ticks;
            string filename = Path.Combine(@"C:\TickPredict\Content\", guess); 
            if (System.IO.File.Exists(filename))
            {
                string contents=System.IO.File.ReadAllText(filename);
                ViewBag.Message = "Success :)<br/> "+contents;
            }
            else {
                ViewBag.Message = "Fail :( ["+ticks+"]";
            }



            return View();
        }
    }
}