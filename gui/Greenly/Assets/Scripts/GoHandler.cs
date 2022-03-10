using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GoHandler : MonoBehaviour
{
    public GameObject ucOne;
    public GameObject ucTwo;
    public InputField searchIn;

    // Start is called before the first frame update
    void Start()
    {
        // initialize and set both false
        ucOne.SetActive(false);
        ucTwo.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        // Use case one 
        if (searchIn.text == "Austin Public Library")
        {
            ucOne.SetActive(false);
            ucTwo.SetActive(true);
        }
        //Use case two
        else if (searchIn.text == "Aloft Hotel")
        {
            ucOne.SetActive(true);
            ucTwo.SetActive(false);
        }
    }



}
