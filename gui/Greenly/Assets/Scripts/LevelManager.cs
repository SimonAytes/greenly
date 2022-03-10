using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.Threading;

public class LevelManager : MonoBehaviour
{
    public int target_scene = 0;
    public bool is_splash = false;


    void Start()
    {
        if (is_splash == true)
        {
            Thread.Sleep(500);
            LoadScene();
        }
    }
    
    // Start is called before the first frame update
    public void LoadScene()
    {
        SceneManager.LoadScene(target_scene);
    }
}
